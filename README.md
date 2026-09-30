# Dice & Card Game Simulator

This is a little Python project I made while learning loops, functions and NumPy. You run it, pick something from a menu, and it rolls dice or draws cards for you and then tells you what came out.

I started with just a dice roller and kept adding stuff because it was fun to see the numbers change every time.

## What it does

You can roll a die as many times as you want, or draw a bunch of random cards. After that it prints out a breakdown: the total, the average, the highest and lowest result, how many times each number showed up (with a row of stars so you can actually see it), which number won the most, and the longest run of the same number in a row.

For cards, the values go A = 1, then 2 to 10 as they are, J = 11, Q = 12 and K = 13.

There's also a small dice game. You roll two dice. If the total is 10 or more you win. If it's exactly 7 it's a draw and you roll again. Anything else and you lose.

And if you've already rolled some dice, you can look at the first few results, the last few, and the whole list flipped backwards.

## Set Up

You need Python 3 and NumPy. If you don't have NumPy yet:


pip install numpy

Then just run the file:

python dice_card_simulator.py

A menu shows up. Type 1, 2, 3, 4 or 0 and hit Enter.

- 1 rolls the dice and analyses them
- 2 draws cards and analyses them
- 3 shows the first, last and reversed results of your last dice roll
- 4 plays the quick dice game
- 0 quits

One thing to know: option 3 only works after you've done option 1, because it needs some dice results to look at. If you go there first it'll just tell you to run option 1.

## What's in the code

It's all in one file, split into small functions so each one does one thing.

- `roll_single_dice` and `draw_single_card`    do the random part
- `dice_rolls` and `card_draws`                repeat that n times and give back a NumPy array
- `counting_frequency`, `summation_of_array` and `longest_streak` are the helpers I wrote by hand to count things
- `analyze_results`                            uses all of those plus a few NumPy functions to print the stats
- `show_first_and_last`                        handles the slicing in option 3
- `play_quick_dice_game`                       is the win/lose/draw game
- `show_menu` and `main`                       run the menu loop

There are a lot of comments in the code because I wrote them to remind myself how things work.

## Stuff I want to fix or add later

Right now if you type a letter where it wants a number, the program crashes. I want to handle that properly. I also want the cards to actually show their suits when they're drawn, and maybe turn it into a real card game at some point.
