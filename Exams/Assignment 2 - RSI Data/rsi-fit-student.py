import pandas as pd
import numpy as np
from scipy.stats import norm, chisquare, ttest_ind, ttest_1samp
import matplotlib.pyplot as plt

"""
Preamble: Load data from source CSV file
"""
path_to_datafile = "../../data/drop-jump/all_participant_data_rsi.csv"

### YOUR CODE HERE
"""
Question 1: Load the force plate and acceleration based RSI data for all participants. Map each data set (accel and FP)
to a normal distribution. Clearly report the distribution parameters (mu and std) and generate a graph two each curve's 
probability distribution function. Include appropriate labels, titles, and legends.
"""
print('-----Question 1-----')
#First I will load the file and make sure that each data point has the corresponding name behind i
data = np.genfromtxt(path_to_datafile, delimiter=',', dtype=None, names=True)
#I will start by finding the mean and standard deviation of the force plate rsi"
fp_mean = np.mean(data["force_plate_rsi"])
fp_std = np.std(data["force_plate_rsi"])
print(f'The RSI force plate data has a mean of {fp_mean}, and a standard deviation of {fp_std}')
#I will do the same for Acceleration
accel_mean = np.mean(data["accelerometer_rsi"])
accel_std = np.std(data["accelerometer_rsi"])
print(f'The RSI Acceleration data has a mean of {accel_mean}, and a standard deviation of {accel_std}')

#Now I plan to find the x and y values for the probability distribution function, and then plot
#Starting with force place:
x_fp = np.linspace(start=min(data["force_plate_rsi"]), stop=max(data["force_plate_rsi"]), num=len(data["force_plate_rsi"]))
y_fp = norm.pdf(x_fp, loc=fp_mean, scale=fp_std)
#Now plot said distribution:
plt.figure()
plt.plot(x_fp, y_fp, label='Fitted Normal')
plt.title('Fitted Normal Probability Distribution for Force Plate RSI')
plt.xlabel('RSI Force Plate')
plt.ylabel('Probability Density')
plt.legend()

#Now with the acceleration data:
x_a = np.linspace(start=min(data["accelerometer_rsi"]), stop=max(data["accelerometer_rsi"]), num=len(data["accelerometer_rsi"]))
y_a = norm.pdf(x_a, loc=accel_mean, scale=accel_std)
#Plot acceleration
plt.figure()
plt.plot(x_a, y_a, label='Fitted Normal')
plt.title('Fitted Normal Probability Distribution for Accelerometer RSI')
plt.xlabel('RSI Accelerometer')
plt.ylabel('Probability Density')
plt.legend()
#Show these graphs
plt.show()
"""
Question 2: Conduct a Chi2 Goodness of Fit Test for each dataset to test whether the data is a good fit
for the derived normal distribution. Clearly print out the p-value, chi2 stat, and an indication of whether it is 
a fit or not. Do this for both acceleration and force plate distributions. It is suggested to generate 9 bins between 
[0,2), add append -inf and +inf to both ends of the bins. An alpha=0.05 is suitable for these tests.
"""
print('\n\n-----Question 2-----')

#I will define the bins first with inf
bins_range = np.linspace(0,2, 8)
#Group it together
bins = np.concatenate(([-np.inf], bins_range, [np.inf]))
"""
Acceleration
"""
#Now lets do the histogram
accel_counts, accel_edges = np.histogram(data["accelerometer_rsi"], bins=bins)
#Compare observed histogram counts to expected counts from fitted normal distribution
cdf_accel = norm.cdf(bins, loc=accel_mean, scale=accel_std)
exp_accel = len(data["accelerometer_rsi"]) * np.diff(cdf_accel)
exp_accel *= sum(accel_counts) / sum(exp_accel)
#Then find the p value and chi2 stat
chi_accel, p_accel = chisquare(accel_counts, exp_accel)
"""
Force Plate
"""
#logic is the same as acceleration
fp_counts, fp_edges = np.histogram(data["force_plate_rsi"], bins=bins)

fp_counts, fp_edges = np.histogram(data["force_plate_rsi"], bins=bins)
#Then find the distribution
cdf_fp = norm.cdf(bins, loc=fp_mean, scale=fp_std)
exp_fp = len(data["force_plate_rsi"]) * np.diff(cdf_fp)
exp_fp *= sum(fp_counts) / sum(exp_fp)
#Then find the p value and chi2 stat
chi_fp, p_fp = chisquare(fp_counts, exp_fp)

"""
Now that the chi2 and p values are found for each, the question can be answered.
"""
alpha = 0.05
print(f"Acceleration: Chi2 = {chi_accel} & p-value = {p_accel}")
if (p_accel > alpha): #Check if fit is good 
    print("Good fit")
else:
    print("Not a good fit")

print()
#repeat for force plate
print(f"Force Plate: Chi2 = {chi_fp} & p-value = {p_fp}")
if (p_fp > alpha):
    print("good fit")
else:
    print("Not a good fit")
"""
Question 3: Perform a t-test to determine whether the RSI means for the acceleration and force plate data are equivalent 
or not. Clearly report the p-value for the t-test and make a clear determination as to whether they are equal or not.
An alpha=0.05 is suitable for these tests.
"""
print('\n\n-----Question 3-----')
#We can start by first using ttest_ind to compare acceleration and force plate data to get a p value and t-statistic
t_stat, p_val = ttest_ind(data["accelerometer_rsi"], data["force_plate_rsi"])
print(f'P-value of t-test: {p_val}')
#Compare p_val to alpha to answer question 3
if p_val > alpha:
    print("These values are equivalent, accept hypothesis")
else:
    print("These values are not equivalent, reject hyptohesis")
"""
Question 4: Calculate the RSI Error for the dataset where error is expressed as the difference between the 
Force Plate RSI measurement and the Accelerometer RSI measurement. Fit this error distribution to a normal curve and 
plot a histogram of the data on the same plot showing the fitted normal curve. Include appropriate labels, titles, and 
legends. The default binning approach from matplot lib with 16 bins is sufficient.
"""
#We will first find the error"
print('\n\n-----Question 4-----')
error = data["force_plate_rsi"] - data["accelerometer_rsi"]
#Then find the average and std
error_mean = np.mean(error)
error_std = np.std(error)
#Report mean and STD"
print(f'Error mean: {error_mean} \nError standard Deviation: {error_std}')

#Now lets plot"
plt.figure()
#Use plt.hist to create the histogram with bins being 16 (listed above)
count, bins, ignored = plt.hist(error, bins=16, density=False, alpha=0.6)
#Create x variables for plot
x_error = np.linspace(min(error),max(error),min((len(data["force_plate_rsi"]), len(data["accelerometer_rsi"]))))
#Create y varaiable for distribution
#It should be noted that scaling is off for the y label so it must be scaled
y_error = norm.pdf(x_error, loc=error_mean, scale=error_std) * len(error) * (bins[1]-bins[0])
#Plot curve
plt.plot(x_error, y_error, label="Fitted Normal Curve")

#Create labels for plot
plt.title("RSI Error Distribution with fit")
plt.xlabel("Error (Force plate - Accelerometer)")
plt.ylabel("Frequency")
plt.legend()

#Show plot
plt.show()