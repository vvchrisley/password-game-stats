import pandas as pd
from captchasums import sums_of_digits, plot_frequency

def main():
    # get video ids from file
    video_ids = pd.read_csv('input/youtube.csv', usecols=['video_id']).squeeze()

    # get the sum of digits in each video id
    sums = sums_of_digits(video_ids)
    print(sums.describe())

    # plot results
    plot_frequency(sums, 'Sum', 'Sum of digits in YouTube video IDs')

if __name__ == '__main__':
    main()
