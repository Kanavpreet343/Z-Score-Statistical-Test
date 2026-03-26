import numpy as np
import matplotlib.pyplot as plt

# Dealing with the observed / gathered data:
observed_data = []
number_of_values = int(input('How many individual data entries: '))

for i in range(number_of_values):
  individual_data = float(input(f'x{i+1}: '))
  observed_data.append(individual_data)

observed_mean = np.mean(observed_data)
observed_stdev = np.std(observed_data, ddof=1)
observed_zscore = observed_mean / observed_stdev

# Dealing with replicated / simulated data:
print('\nThe range is between 1-10000 for it to run smoothly, and 100000 max:')
num_replicas = int(input('Number of Replicas to Simulate = '))
num_samples = len(observed_data)
a = (-1)*((observed_stdev*np.sqrt(12))/2)
b = ((observed_stdev*np.sqrt(12))/2)

# 1. Replicate the experiment by treating U(alpha, beta) as the TRUE distribution of the data
rng = np.random.default_rng()
replicas = [
    rng.uniform(a, b, num_samples)
    for i in range(num_replicas)
]

# 2. For each replica, calculate the z-score with respect to
#    the observed standard deviation so that we can make apple-to-apple comparisons.
simulated_zscores = [
    np.mean(replica) / np.std(replica, ddof=1)\
    for replica in replicas
]

# 3. Count the number of simulated false positive.
# A replica is a false positive if its z-score is bigger than the observed z-score.

num_false = sum(
    1
    for z in simulated_zscores
    if np.abs(z) > np.abs(observed_zscore) # compare z-scores
)
prob = num_false / num_replicas

# Printing
print(f"\nData Gathered:\n{observed_data}\n\n"\
      f"Mean = {observed_mean}\n"\
      f"Standard Deviation = {observed_stdev}\n"\
      f"Z-Score for Observed Data = {observed_zscore}\n\n"\
      f"Number of False Positives: {num_false}\n"\
      f"Probability of False Positives: {prob}, {100*prob}%\n")

# Plotting Observed and Generated Data
plt.hist(simulated_zscores, 100)
plt.title("distribution of simulated $z$-scores - Null Model")
plt.xlabel("$z$-scores")
plt.ylabel("count")
plt.show()

# First, plot the histogram as you already do
counts, bins, patches = plt.hist(simulated_zscores, bins=100, alpha=0.7, color='grey')
plt.xlabel("$z$-scores")
plt.ylabel("Count")
plt.title("Distribution of simulated $z$-scores - Null Model")

# Overlay observed z-score with SD
y_position = max(counts) * 0.8  
plt.errorbar(
    observed_zscore,      
    y_position,           
    xerr=observed_stdev,  
    fmt='o',              
    capsize=5,
    color='blue',
    label='Observed z-score ± SD'
)

plt.legend()
plt.show()

print('\nWHAT THE MODEL REPRESENTS:')
print('This is a Null Model: this is what the data should look like if nothing special is happening; if the Null Hypothesis is True')
print('The expectancy is 0 because in long run, we expect nothing to happen\n')

print('WHAT THE AXIS REPRESENT:')
print('The x-axis represents the z-score:')
print('This represents how far the result is from the Null-mean\n')
print('The y-axis represents frequency of various z-scores')
print('This shows how many simulated datasets produced that specific z-score\n')

print('HOW TO USE THE MODEL AS STATISTICAL TEST FOR NULL HYPOTHESIS:')
print('Example: if you are running a drug trial, and your data\'s mean sits in')
print('the middle, then the experiment is not significant, the result was due')
print('to random noise. But if the mean corresponds to data near the tails,')
print('then the experiment has rare, statistically significant values to observe.\n')

print('HOW TO USE THE MODEL AS DETECTING FALSE POSITIVES:')
print('Its also important to note false positives. With this graph, we must ask')
print('if the mean was gathered by chance, and the drug really did nothing, then')
print('how often would we see results that look this rare (i.e false positives)?')
print('If the drug truly does nothing, then all values to the right of (+mean) would')
print('be false positives, and all values to the left of (-mean) would be false positives.\n')

print('FINAL NOTE:')
print('Lastly, the \'means\' I talk about is the z-score of the observed dataset\'s mean!')
print(f'This is \'z-Score for observed Data = {observed_zscore}\' We can relate this to false positives.')
if prob < 0.05:
  print('The observed z-score is so high (relatively). This makes sense since the probability')
  print('of false positives is so low, confirming that the reason for variance is not random noise,')
  print('and the high z-score is far from 0, further confirming that variance is rare, and is attributed to a cause')
else:
  print('The observed z-score is so low (relatively). This makes sense since the probability')
  print('of false positives is so high, confirming that the reason for any variance is random noise,')
  print('and the low z-score is close to 0, further confirming that the variance is attributed to random noise.')
