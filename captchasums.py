import pandas as pd

def sum_of_digits(string):
    """Return the sum of all digits in a string. 
    >>> sum_of_digits("2b827")
    19
    """
    return sum(int(char) for char in string if char.isdigit())

def main():
    # get captchas from file
    captcha_list = open('input/captchas', 'r').read().split(',')

    # get the sum of digits in each captcha
    sums = pd.Series([sum_of_digits(captcha) for captcha in captcha_list])

    # print results
    print("Total CAPTCHAs:", len(captcha_list), "\n")
    print("sum  # of CAPTCHAs")
    print(sums.value_counts().sort_index())

if __name__ == '__main__':
    main()
