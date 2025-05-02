import pandas as pd 
import matplotlib.pyplot as plt
from captchasums import sum_of_digits

def main():
    # set plot labels
    plt.title("Sum of digits in YouTube video IDs")
    plt.xlabel("Sum")
    plt.ylabel("Frequency")

    # get video ids from file
    video_ids = pd.read_csv('input/youtube.csv', usecols=['video_id']).squeeze()

    # get the sum of digits in each video id
    sums = pd.Series([sum_of_digits(vid_id) for vid_id in video_ids])
    sum_counts = sums.value_counts().sort_index()
    print(sums.describe())

    # plot results
    plt.bar(sum_counts.index, sum_counts)
    plt.show()

if __name__ == '__main__':
    main()