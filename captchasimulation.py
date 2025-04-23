import random
import numpy as np
import matplotlib.pyplot as plt

# set plot labels
plt.title("Refreshes until CAPTCHA with no digits")
plt.xlabel("Number of refreshes")
plt.ylabel("Frequency")

# probability of getting desired result on one attempt
chance_of_result = 12/149
# estimated time it takes to try for the result in real life
seconds_per_attempt = 1
# number of times to run the simulation
num_trials = 10000

def run_trial():
  """Simulate trying for the desired result until you get it.
  Return how many attempts it took."""
  attempts = 0
  result = random.random()
  while (not result < chance_of_result):
    result = random.random() 
    attempts += 1
  return attempts

# run simulation the specified number of times
attempts_per_trial = [run_trial() for trial in range(num_trials)]

# print average number of attempts until desired result
avg_attempts = np.mean(attempts_per_trial)
print("Average # of attempts:", avg_attempts)

# print estimated time until desired result
time = avg_attempts * seconds_per_attempt
print(time // 60, "minutes", time % 60, "seconds")

# plot the data
plt.hist(attempts_per_trial, bins=range(max(attempts_per_trial)))
plt.show()
