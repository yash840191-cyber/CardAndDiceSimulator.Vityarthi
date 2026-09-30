import random       # for generating random numbers/choices 
import numpy as np

SUITS = ["Hearts" , "Diamonds" ,  "Spades" ,  "Clubs"]  
RANKINGS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"] 
RANKINGS_VALUES = {
    "A":  1,
    "2":  2,
    "3":  3,
    "4":  4,
    "5":  5,
    "6":  6,
    "7":  7,
    "8":  8,
    "9":  9,
    "10": 10,
    "J":  11,
    "Q":  12,
    "K":  13
    #This was a dictionary made with key:value pair
}

def roll_single_dice():
    """rolls one fair six-sided die."""
    return random.randint(1 , 6)  #a die has faces 1 through 6, so we want random.randint(1, 6), not random.randint(1, 5) 

def draw_single_card():
    """draws one random card and hand back both its rank and its suit"""
    suit = random.choice(SUITS)
    rank = random.choice(RANKINGS)
    return rank , suit

#random.choice(a_list) — picks one random item from a list. You already have SUITS and RANKS as lists

def dice_rolls(n):
    results = []                          #creates the empty list 
    for _ in range(n):
        results.append(roll_single_dice())
    return np.array(results)              #runs after the loop completes

def card_draws(n):
    numeric_values = []
    full_cards = []
    for _ in range (n):
        rank , suit = draw_single_card()
        numeric_values.append(RANKINGS_VALUES[rank])
    return np.array(numeric_values), full_cards #the numeric list converted to a NumPy array (for stats), and the full_cards list left as a plain Python list 
def counting_frequency(results_array, value):    #counts the number of times a number is occuring 
    count = 0
    for item in results_array:
        if item == value:
            count += 1
    return count    

def summation_of_array(results_array):   #adds the outcomes
    total = 0
    for item in results_array:
        total += item 
    return total 

def longest_streak(results_array):       #the long streak function is defined for length 
    if len (results_array) == 0:
        return 0, None

    longest = 1 
    current = 1
    best_value = results_array[0]

    for i in range(1 , len(results_array)):
        if results_array[i] == results_array[i - 1]:
            current += 1
            if current > longest:
               longest = current
               best_value = results_array[i]

        else:
            current = 1

    return longest, best_value

def analyze_results(results_array, label):
    print(f"\n--- {label}: Array Analytics (NumPy) ---")
    print(f"Raw results array: {results_array}")
    
    print(f"Sum (np.sum): {np.sum(results_array)}")
    print(f"Mean (np.mean): {np.mean(results_array):.2f}") #:.2f rounds off to 2 decimal places for display.
    print(f"Max (np.max): {np.max(results_array)}")
    print(f"Min (np.min): {np.min(results_array)}")
    print(f"Total VALUE: {results_array.size}")

    unique_values = sorted(set(results_array.tolist()))   #to get distinct values through all the results...
    most_common_value = unique_values[0]
    highest_freq = 0
    print("\nFrequency Distribution:")
    for value in unique_values:
        freq = counting_frequency(results_array, value)
        bar = "*" * freq
        print(f" {value:>3}: {freq:<3} {bar}")
        if freq > highest_freq:
            highest_freq = freq
            most_common_value = value

    print(f"\nMost common result: {most_common_value} (appeared {highest_freq} times)")
    
    streak_len, streak_val =longest_streak(results_array)                   #this is used to get two return values 
    print(f"Longest streak: {streak_len} in a row (value = {streak_val})")
    avg = np.mean(results_array)
    above_avg_indices = np.where(results_array > avg)[0]
    print(f"Rolls/draws above average ({avg:.2f}): {len(above_avg_indices)} out of {results_array.size}")
   
def show_first_and_last(results_array, n=5):
    print(f"First    {n}  results:   {results_array[:n]}"  )
    print(f"Last     {n}  results:   {results_array[-n:]}" )
    print(f"Reversed {n}  results:   {results_array[::-1]}")

def play_quick_dice_game():
    """while True loop is used here because we don't know how many times we have to re-roll on a draw"""
    print("Rule explanation here...")

    while True:
        d1 = roll_single_dice()
        d2 = roll_single_dice()
        total = d1 + d2
        print(f"You rolled: {d1} + {d2} = {total}")

        if total >= 10:
            print("Result: You WIN!")
            break
        elif total == 7:
            print("Result: DRAW - rolling again...")
            continue
        else:
            print("Result: You LOSE.")
            break

def show_menu():
    print("\n" + "=" * 55)
    print(" DICE & CARD GAME SIMULATOR")
    print("=" * 55)
    print(" 1. Simulate Dice Rolls + Full Analysis")
    print(" 2. Simulate Card Draws + Full Analysis")
    print(" 3. Show First/Last/Reversed Slice of Last Dice Thrown")
    print(" 4. Play Quick Dice Game (Win/Lose/Draw)")
    print(" 0. Exit")
    print("=" * 55)    

def main():
    print("Welcome to the Dice & Card Game Simulator!")
    last_dice_results = None                              # will hold results from option 1, for use in option 3

    while True:
        show_menu()
        choice = input("Please Enter your choice: ").strip()

        if choice == "1":
            n = int(input("How many times should the dice be rolled?"))                  # ask number of rolls.
            last_dice_results = dice_rolls(n)
            analyze_results(last_dice_results, "Dice Rolls")                             # then call analyze_results() on it 
            

        elif choice == "2":
            # asks number of draws
             n = int(input("How many cards should be drawn? "))
             values_array, cards = card_draws(n)
             analyze_results(values_array, "Card Draws")


        elif choice == "3":
            if last_dice_results is None:
                print("Run option 1 first to generate dice results!")


            else:
                show_first_and_last(last_dice_results)


        elif choice == "4":
            play_quick_dice_game()


        elif choice == "0":
            print("Thanks for playing!")
            break


        else:
            print("Invalid, Please try again.")


if __name__ == "__main__":
    main()
        















































































































































































































