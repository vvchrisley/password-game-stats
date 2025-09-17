# The Password Game: Strategy and statistics

[The Password Game](https://neal.fun/password-game/) is a game by Neal Agarwal where you must create a password that meets increasingly absurd requirements.
Many of the rules build on each other, such that satisfying one could invalidate a previous rule. It's definitely possible to beat the game, though, and
the statistics show it! The Python libraries I used were:

- [Pandas](https://pandas.pydata.org/) for reading and manipulating data
- [Matplotlib](https://matplotlib.org/) for visualization
- [SciPy](https://scipy.org/) for statistical functions

## CAPTCHAs

One rule requires your password to contain a randomly chosen CAPTCHA. Combined with the requirement that the digits in your password add to 25, this
presents one of the first hurdles for many players. You might notice that you're allowed to refresh the CAPTCHA and get a new one, but what a lot of players
don't realize at first is that it doesn't take long to get a CAPTCHA with no digits at all--in fact, it takes about 28 seconds.

Twelve of the 149 CAPTCHAs have no digits, which I found with [captchasums.py](https://github.com/vvchrisley/password-game-stats/blob/main/captchasums.py). The 
number of attempts at a random event until getting a certain outcome follows a [geometric distribution](https://en.wikipedia.org/wiki/Geometric_distribution), so 
in [captchasimulation.py](https://github.com/vvchrisley/password-game-stats/blob/main/captchasimulation.py) I used that to show that 90% of the time, you'll have
to refresh the CAPTCHA no more than 28 times before getting one with no digits.

(Fun fact, the CAPTCHAs used in the game appear to be a random sample from [this dataset](https://www.kaggle.com/datasets/fournierp/captcha-version-2-images).)

## Chess puzzles

In [chesselements.py](https://github.com/vvchrisley/password-game-stats/blob/main/chesselements.py), I did a couple things. For one, I showed that 95% of the time,
the "best move" is one that puts your opponent in check, so even if you're not a chess player you can just learn how the pieces are allowed to move and try all of
the moves that would get you one move away from capturing their king. Another thing I found is that 10% of the puzzles have a solution that contains Bh, Nh, Rf, or 
Rg--all symbols for elements with an atomic number over 100. That does mean 90% of the puzzles shouldn't cause you much trouble, but if you get one of those 
high-numbered elements in your chess move, you'll probably want to start the game over.

## Hex colors

Much of the same code used to make the CAPTCHA calculations can be used here, but unlike the CAPTCHAs, there are 16,777,216 possible colors and only 0.7% of them
have no digits. If you're patient, you *could* try refreshing the color about 144 times until you get one. Most likely, you'll be fine with one that has a sum
of no more than 5, which will take only 15 tries on average.

## YouTube URLs

With [youtubesums.py](https://github.com/vvchrisley/password-game-stats/blob/main/youtubesums.py), I found that a *lot* of YouTube URLs have no digits in them,
and that when they do, they tend to have a pretty low sum--half of YouTube URLs have digits that add up to 7 or less, and 75% of them to 14 or less. Anecdotally,
the much more difficult constraint is finding one without heavy atomic symbols, but maybe next I'll prove that's not so hard either, haha.
