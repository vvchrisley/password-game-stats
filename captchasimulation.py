from scipy.stats import geom

def main():
  # probability of desired outcome
  prob = 12/149

  # approximate time it takes to try for the result in real life
  seconds_per_attempt = 1

  # max time it will take 75% and 90% of the time
  est_75 = geom.ppf(0.75, prob) * seconds_per_attempt
  est_90 = geom.ppf(0.90, prob) * seconds_per_attempt

  # print results
  print("Getting a CAPTCHA with no digits will take less than")
  print(int(est_75 // 60), "minutes", est_75 % 60, "seconds 75% of the time")
  print(int(est_90 // 60), "minutes", est_90 % 60, "seconds 90% of the time")

if __name__ == '__main__':
  main()
