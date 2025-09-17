# password-game-stats

Some scripts I used while [analyzing The Password Game](https://vvchrisley.github.io/password-game-stats) (which you can [play on neal.fun](https://neal.fun/password-game/)).

## Use

Download the files from this repository, then download these two data sets from Kaggle:

- [Hydrogen to Oganesson: Periodic Insights](https://www.kaggle.com/datasets/kanchana1990/hydrogen-to-oganesson-periodic-insights) as **input/elements.csv**
- US_youtube_trending_data.csv from [YouTube Trending Video Dataset](https://www.kaggle.com/datasets/rsrishav/youtube-trending-video-dataset?select=US_youtube_trending_data.csv) as **input/youtube.csv**

Now as long as you have Python installed, you can run any of the scripts with `python scriptname.py`

### captchasums

Takes the list of CAPTCHAs used in game, calculates the sum of digits in each one, and plots how frequent each sum is.

### captchasimulation

When you repeatedly refresh the CAPTCHA in game to get one with no digits, how many refreshes it will take follows a geometric distibution. This script estimates how long it will take.

### chesselements

Takes the list of chess puzzles used in game and finds how many of their solutions contain atomic symbols, and what the atomic weight of those elements are. Also spits out how many of the moves end in check--knowing that it's most of them makes it quicker to figure out the solution while playing.

### youtubesums

Prints some statistics about the sum of digits in YouTube URLs.
  
