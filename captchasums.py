import re
import pandas as pd

# get captchas from file
captcha_list = open('captcha_stuff/captchas', 'r').read().split(',')

def sum_of_digits(string):
    """Return the sum of all digits in a string. 
    >>> sum_of_digits("2b827")
    19
    """
    digits = re.findall(r'\d', string)
    return sum(int(digit) for digit in digits)

# get the sum of digits in each captcha
sums = [sum_of_digits(captcha) for captcha in captcha_list]

# print results
print("# of CAPTCHAs:", len(captcha_list))
print(pd.value_counts(sums).sort_index())
