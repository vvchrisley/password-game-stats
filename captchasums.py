import pandas as pd
import matplotlib.pyplot as plt

def sums_of_digits(str_list):
    """Return the sum of digits in each string in a list. 
    >>> sum_of_digits(['2b827', '3bfnd'])
    0   19
    1   3
    Length: 2, dtype: int64
    """
    sum_digits = lambda s: sum(int(char) for char in s if char.isdigit())
    return pd.Series([sum_digits(string) for string in str_list])

def plot_frequency(series, xlabel='Value', title='Value counts'):
    """Graph the frequency of items in a Series."""
    data = series.value_counts()
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel('Frequency')
    plt.bar(data.index, data)
    plt.show()

def main():
    # get captchas from file
    captcha_list = open('input/captchas', 'r').read().split(',')

    # get captcha sums
    sums = sums_of_digits(captcha_list)
    
    # plot results
    title = 'Sum of digits in CAPTCHAs (n = ' + str(len(captcha_list)) + ')'
    plot_frequency(sums, 'Sum', title)

if __name__ == '__main__':
    main()
