# Project Statement: Dice & Card Game Simulator

## 1. Introduction

This is my Python project where I built a small **Dice & Card Game Simulator** that runs in the terminal. It lets the user roll dice, draw cards, look at simple statistics of the results, and play a quick dice game. I made this project to practice the basics of Python that I have learned so far, such as functions, loops, lists, dictionaries, and the NumPy library.

## 2. Problem Statement

Random events like rolling a die or drawing a card are easy to do but hard to understand when we only look at raw numbers. If someone rolls a die 50 times, it is difficult to see at a glance which number came most often, what the average was, or whether the same number came many times in a row.

The problem I wanted to solve is:

> *Build a menu-driven program that can simulate random dice rolls and card draws, store the results, analyse them (sum, mean, min, max, frequency, streaks), and also let the user play a simple dice game.*

## 3. Objectives

- To simulate a fair six-sided die and a deck of cards using Python's `random` module.
- To store results in NumPy arrays so that statistics can be calculated easily.
- To write my own logic (without only relying on built-in functions) for counting frequency, summing values, and finding the longest streak.
- To display the frequency of each result as a simple text bar chart.
- To create a menu so that the user can choose what to do repeatedly until they exit.
- To practice writing small, reusable functions with docstrings and comments.

## 4. Features

The program shows this menu:

| Option | What it does |
|--------|--------------|
| 1 | Rolls the dice *n* times and shows a full analysis |
| 2 | Draws *n* cards and shows a full analysis of their values |
| 3 | Shows the first 5, last 5, and reversed results of the last dice roll |
| 4 | Plays a quick dice game (Win / Lose / Draw) |
| 0 | Exits the program |

### Analysis shown for options 1 and 2
- The raw results array
- Sum, mean, maximum and minimum (using NumPy)
- Total number of values
- Frequency distribution with `*` bars
- Most common result
- Longest streak (same value repeated in a row)
- How many results were above the average

### Rules of the quick dice game
Two dice are rolled and added together.
- Total **10 or more** → **You WIN**
- Total **exactly 7** → **DRAW**, so the dice are rolled again
- Any other total → **You LOSE**

### Card values
Each rank is given a number using a dictionary: `A = 1`, `2` to `10` are their own numbers, `J = 11`, `Q = 12`, `K = 13`.

## 5. Concepts Used

- **Variables, lists and dictionaries**: `SUITS`, `RANKINGS` and `RANKINGS_VALUES`
- **Functions**: each task has its own function, such as `roll_single_dice()` and `draw_single_card()`
- **Loops**: `for` loops for repeating rolls, and `while True` loops for the menu and the game (because we don't know how many times the user will re-roll or choose)
- **Conditionals**: `if / elif / else` for menu choices and game results
- **Random module**: `random.randint()` and `random.choice()`
- **NumPy**: `np.array`, `np.sum`, `np.mean`, `np.max`, `np.min`, `np.where`, and array slicing
- **Slicing**: `[:n]`, `[-n:]` and `[::-1]` for first, last and reversed results
- **f-strings**: for formatted output like `{avg:.2f}`
- **Tuple returns**: functions returning two values, like `longest_streak()` and `card_draws()`

## 6. How the Program Works

1. `main()` starts the program and keeps showing the menu inside a `while True` loop.
2. When the user picks option 1, `dice_rolls(n)` rolls the die `n` times and returns a NumPy array.
3. `analyze_results()` then prints all the statistics for that array.
4. Option 2 works the same way, but `card_draws(n)` converts each drawn card into its number value first.
5. Option 3 uses the saved dice results (`last_dice_results`). If option 1 has not been run yet, the program tells the user to run it first.
6. Option 4 calls `play_quick_dice_game()`.
7. Option 0 breaks the loop and ends the program.

## 7. How to Run

Requirements: Python 3 and NumPy.

```bash
pip install numpy
python main.py
```

(Replace `main.py` with whatever the file is named.)

## 8. Sample Interaction

```
Please Enter your choice: 1
How many times should the dice be rolled?10

--- Dice Rolls: Array Analytics (NumPy) ---
Raw results array: [3 5 5 2 6 1 4 4 4 2]
Sum (np.sum): 36
Mean (np.mean): 3.60
...
```

*(The numbers will be different every time because they are random.)*

## 9. Limitations / Things I Noticed

- If the user types something that is not a number when asked for `n`, the program will crash with a `ValueError`. I need to add input validation with `try / except`.
- In `card_draws()`, the `full_cards` list is created but I forgot to add the (rank, suit) pairs into it, so it always comes back empty. Only the numeric values are used right now.
- The card draws are independent, so the same card can appear again and again like drawing from an infinite deck, not a real 52-card deck.
- The rule message in the dice game still says `"Rule explanation here..."` and needs to be replaced with the actual rules.
- In `analyze_results()`, if two values have the same highest frequency, only the smaller one is reported as the most common.

## 10. Future Improvements

- Add input validation so the program never crashes on wrong input.
- Use a real 52-card deck that is shuffled, and remove cards after they are drawn.
- Store and show the actual card names, like "K of Hearts".
- Add a graph using `matplotlib` instead of the `*` bars.
- Keep a score history for the dice game.
- Allow the user to choose the number of sides on the die.

## 11. What I Learned

Through this project I learned how to break a big problem into small functions, how to use NumPy arrays instead of plain lists for calculations, and how loops and conditions work together in a menu-driven program. I also learned that reading the code again carefully shows small mistakes, like the empty `full_cards` list, which I would like to fix next.

## 12. Conclusion

This project helped me understand how randomness and basic statistics can be simulated with Python. It is a simple program, but it gave me good practice with the core concepts, and I plan to keep improving it as I learn more.
