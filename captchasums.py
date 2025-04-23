import re

# track how many captchas have what sums
sum_counts = [0] * 26

# get captchas from file
captcha_list = open('input/captchas', 'r').read().split(',')
# remove quotation marks
captcha_list = [captcha.strip('"') for captcha in captcha_list]

for captcha in captcha_list:
    # sum digits from captcha
    digits = re.findall(r'\d', captcha)
    sum_of_digits = sum(int(digit) for digit in digits)
    # increment the appropriate sum count
    if sum_of_digits < 25:
        sum_counts[sum_of_digits] += 1
    else:
        sum_counts[25] += 1

# print results
print("Total CAPTCHAs:", sum(sum_counts), "\n")
print("Sum:\t# of CAPTCHAs:")
for i, count in enumerate(sum_counts[0:25]):
    print(i, "\t", count)
print(">=25\t", sum_counts[25])
