import random
import pandas as pd
import matplotlib.pyplot as plt

def attempts_until(prob_outcome):
  """Given the probability of an outcome, simulate making repeated
  attempts until acheiving it. Return how many attempts it took."""
  attempts = 0
  result = random.random()
  while (not result < prob_outcome):
    result = random.random() 
    attempts += 1
  return attempts

def monte_carlo(prob_outcome, num_trials):
  """Return a list of how many attempts it took to achieve
  an outcome with the given probability in each of the given
  number of trials."""
  return [attempts_until(prob_outcome) for trial in range(num_trials)]

def main():
  # simulate refreshing captcha until getting one with no digits
  attempts_per_trial = monte_carlo(12/149, 10000)

  # estimated time it takes to try for the result in real life
  seconds_per_attempt = 1
  time_per_trial = pd.Series([attempts * seconds_per_attempt 
  for attempts in attempts_per_trial])

  # print results
  pct_75 = time_per_trial.quantile(0.75)
  pct_90 = time_per_trial.quantile(0.9)
  print("Getting a CAPTCHA with no digits will take less than")
  print(int(pct_75 // 60), "minutes", pct_75 % 60, "seconds 75% of the time")
  print(int(pct_90 // 60), "minutes", pct_90 % 60, "seconds 90% of the time")

  # plot the data
  plt.title("Refreshes until CAPTCHA with no digits")
  plt.xlabel("Number of refreshes")
  plt.ylabel("Frequency")
  plt.hist(attempts_per_trial, bins=range(max(attempts_per_trial)))
  plt.show()

if __name__ == '__main__':
  main()
