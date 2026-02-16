# bring in randomness cause we need it in our lives
import random

### Begin Dr. Forsyth Code. Do Not Modify ###

# copy in Dr. Forsyth's random list function for use
def generate_random_int_list(max_length, upper_bound):
    # generate random length between 2 and max_length
    list_length = int(random.uniform(2, max_length))

    # given the length above, sample the Natural Numbers up to upper_bound that many times
    vars = random.sample(range(upper_bound), list_length)

    # return the generated list
    return vars


# set the maximum length of the list
max_length = 100

# set the maximum upper bound for the list
upper_bound = 1000

# generate a random lists of integers
nums = generate_random_int_list(max_length, upper_bound)
evens_list = []
odds_list = []
for i in nums:
    check = i % 2
    if check == 1: #this means it is odd
        odds_list.append(i)
    elif check == 0:
        evens_list.append(i)
# create two variables to hold the final answers
num_evens = len(evens_list)
num_odds = len(odds_list)
print(nums)
print(num_evens, num_odds)
### YOUR CODE BEGINS HERE ###