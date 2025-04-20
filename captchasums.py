import re

# track how many captchas have what sums
sum_counts = [0] * 26

# capture from captchas file (one line of alphanum strings enclosed in quotes)
captcha_list = open("captchas", "r").readline()
pattern = re.compile(r"\"([a-z0-9]+)\"")

# for each captcha, sum the digits in it
for match in re.finditer(pattern, captcha_list):
    sum_of_digits = sum(int(char) for char in match.group(1) if char.isdigit())
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