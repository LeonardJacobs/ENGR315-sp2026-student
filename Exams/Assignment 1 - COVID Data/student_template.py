import sys


def parse_nyt_data(file_path=''):
    """
    Parse the NYT covid database and return a list of tuples. Each tuple describes one entry in the source data set.
    Date: the day on which the record was taken in YYYY-MM-DD format
    County: the county name within the State
    State: the US state for the entry
    Cases: the cumulative number of COVID-19 cases reported in that locality
    Deaths: the cumulative number of COVID-19 death in the locality

    :param file_path: Path to data file
    :return: A List of tuples containing (date,county, state, fips, cases, deaths) information
    """
    # data point list
    data=[]

    # open the NYT file path
    try:
        fin = open(file_path)
    except FileNotFoundError:
        print('File ', file_path, ' not found. Exiting!')
        sys.exit(-1)

    # get rid of the headers
    fin.readline()

    # while not done parsing file
    done = False

    # loop and read file
    while not done:
        line = fin.readline()

        if line == '':
            done = True
            continue

        # format is date,county,state,fips,cases,deaths
        (date,county, state, fips, cases, deaths) = line.rstrip().split(",")

        # clean up the data to remove empty entries
        if cases=='':
            cases=0
        if deaths=='':
            deaths=0

        # convert elements into ints
        try:
            entry = (date,county,state, fips, int(cases), int(deaths))
        except ValueError:
            print('Invalid parse of ', entry)

        # place entries as tuple into list
        data.append(entry)


    return data

def first_question(data):
    """
    # Write code to address the following question: Use print() to display your responses.
    # When was the first positive COVID case in Rockingham County?
    # When was the first positive COVID case in Harrisonburg?
    :return:
    """
    #initilialize list
    county = []
    town = []
    # examine each case and see if said case is in Harrisonburg or Rockingham County
    for i in range(len(data)):
        if (data[i][1] == "Rockingham") & (data[i][2] == "Virginia"):
            county.append(data[i])
        if data[i][1] == "Harrisonburg city":
            town.append(data[i])
    # store the first cases in a list 
    firstCase = [county[0], town[0]]
    # print out the answer
    print(f'The first positive COVID 19 case in Rockingham County was on {firstCase[0][0]}')
    print(f'The first positive COVID 19 case in Harrisonburg was on {firstCase[1][0]}')
    return

def second_question(data):
    """
    # Write code to address the following question: Use print() to display your responses.
    # What day was the greatest number of new daily cases recorded in Harrisonburg?
    # What day was the greatest number of new daily cases recorded in Rockingham County?
    :return:
    """
    # Similar approach as the first question, but the 2nd half will be different
    # Initilialize list
    county = []
    town = []
    # examine each case and see if said case is in Harrisonburg or Rockingham County
    for i in range(len(data)):
        if (data[i][1] == "Rockingham") & (data[i][2] == "Virginia"):
            county.append(data[i])
        if data[i][1] == "Harrisonburg city":
            town.append(data[i])
    # Initialize a max cases variable to compare
    maxCountyCases = 0
    # Set a previous value to find daily cases
    previous = 0
    for x in county:
        dailyCases = int(x[4]) - previous
        previous = int(x[4])
        if dailyCases > maxCountyCases:
            maxCountyCases = dailyCases
            index = county.index(x)
    # Print out the answer
    print(f'The greatest amount of daily COVID cases in Rockingham county was {maxCountyCases} cases on {county[index][0]}')
    
    # Code is repeated for Harrisonburg
    maxCountyCases = 0
    # Set a previous value to find daily cases
    previous = 0
    for x in town:
        dailyCases = int(x[4]) - previous
        previous = int(x[4])
        if dailyCases > maxCountyCases:
            maxCountyCases = dailyCases
            index = town.index(x)
    # Print out the answer
    print(f'The greatest amount of daily COVID cases in Harrisonburg was {maxCountyCases} cases on {town[index][0]}')
    return

def third_question(data):
    """
    # Write code to address the following question: Use print() to display your responses.
    # What was the worst 7-day period in either the city and county for new COVID cases?
    # This is the 7-day period where the number of new cases was maximal.
    :return:
    """
    # Similar approach as the first question, but the 2nd half will be different
    # Initilialize list
    county = []
    town = []
    # examine each case and see if said case is in Harrisonburg or Rockingham County
    for i in range(len(data)):
        if (data[i][1] == "Rockingham") & (data[i][2] == "Virginia"):
            county.append(data[i])
        if data[i][1] == "Harrisonburg city":
            town.append(data[i])
    # Find Daily case numbers
    
    # Set a previous value to find daily cases
    # Starting with Rockingham...
    previous = 0
    daily = []
    for x in county:
        dailyCases = int(x[4]) - previous
        previous = int(x[4])
        daily.append(dailyCases)
    # Find 7-day sums
    caseSum = 0
    caseIndex = 0
    for i in range(len(daily) - 6):
        totalSum = sum(daily[i:i+7])
        if totalSum > caseSum:
            caseSum = totalSum
            caseIndex = i

    # Find the start and stop days of the 7 day period
    start = county[caseIndex][0]
    end = county[caseIndex + 6][0]
    print(f'The worst 7-day period COVID-19 cases in Rockingham County was {caseSum} total cases from {start} to {end}')

    # The same logic is repeated for Harrisonburg
    previous = 0
    daily = []
    for x in town:
        dailyCases = int(x[4]) - previous
        previous = int(x[4])
        daily.append(dailyCases)
    # Find 7-day sums
    caseSum = 0
    caseIndex = 0
    for i in range(len(daily) - 6):
        totalSum = sum(daily[i:i+7])
        if totalSum > caseSum:
            caseSum = totalSum
            caseIndex = i

    # Find the start and stop days of the 7 day period
    start = town[caseIndex][0]
    end = town[caseIndex + 6][0]
    print(f'The worst 7-day period COVID 19 cases in Harrisonburg was {caseSum} total cases from {start} to {end}')
    return

if __name__ == "__main__":
    data = parse_nyt_data('us-counties.csv')

    # for (date,county, state, fips, cases, deaths) in data:
    #     print('On ', date, ' in ', county, ' ', state, ' there were ', cases, ' cases and ', deaths, ' deaths')


    # write code to address the following question: Use print() to display your responses.
    # When was the first positive COVID case in Rockingham County?
    # When was the first positive COVID case in Harrisonburg?
    first_question(data)


    # write code to address the following question: Use print() to display your responses.
    # What day was the greatest number of new daily cases recorded in Harrisonburg?
    # What day was the greatest number of new daily cases recorded in Rockingham County?
    second_question(data)

    # write code to address the following question: Use print() to display your responses.
    # What was the worst seven day period in Harrisonburg for new COVID cases (in terms of absolute number of cases)?
    # What was the worst seven day period in Rockingham County for new COVID cases (in terms of absolute number of cases)?
    third_question(data)


