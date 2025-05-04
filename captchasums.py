import pandas as pd
import matplotlib.pyplot as plt

def sum_of_digits(string):
    """Return the sum of all digits in a string. 
    >>> sum_of_digits('2b827')
    19
    """
    return sum(int(char) for char in string if char.isdigit())

def main():
    # get captchas from file
    captcha_list = open('input/captchas', 'r').read().split(',')

    # get the sum of digits in each captcha
    sums = pd.Series([sum_of_digits(captcha) for captcha in captcha_list])
    sum_counts = sums.value_counts().sort_index()
    
    # plot results
    num_captchas = str(len(captcha_list))
    title = 'Sum of digits in CAPTCHAs (n = ' + num_captchas + ')'
    plt.title(title)
    plt.xlabel('Sum')
    plt.ylabel('Frequency')
    plt.bar(sum_counts.index, sum_counts)
    plt.show()

if __name__ == '__main__':
    main()
