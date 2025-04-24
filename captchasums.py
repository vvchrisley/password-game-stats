import re
import pandas as pd

# track how many captchas have what sums
sum_counts = pd.DataFrame({'count': [0] * 26}, index=list(range(25))+['>=25'])

# get captchas from file
captcha_list = open('input/captchas', 'r').read().split(',')

for captcha in captcha_list:
    # sum digits from captcha
    digits = re.findall(r'\d', captcha)
    sum_of_digits = sum(int(digit) for digit in digits)
    # increment the appropriate sum count
    if sum_of_digits < 25:
        sum_counts['count'][sum_of_digits] += 1
    else:
        sum_counts['count']['>=25'] += 1

# print results
print("Total CAPTCHAs:", sum(sum_counts['count']), "\n")
print(sum_counts)
