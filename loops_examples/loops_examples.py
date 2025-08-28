""" A Function with a List comprehension "Prints list char, that are not vowel" """

def is_not_vowel(letter):
    """Returns True if the letter is not a vowel."""
    vowels = "aeiouy"
    return letter.lower() not in vowels

sentence = "hello world"
consonants = [char for char in sentence if is_not_vowel(char)]
print(consonants)

"""1. For loop - Sum all numbers from 1 to 100"""

total = 0
for i in range(1, 101):
    total += i
print (total)

"""2. Print the squares of even numbers from 0 to 20"""

numbers = range(21)
even_numbers = [n**2 for n in numbers if n % 2 == 0]
print(even_numbers)

"""List comprehension"""

squares = [x**2 for x in range(10)] 
print(squares)

"""A function with loop List modification"""

def modify_list(lst):
    """Returns a multiplication of list mnumbers.""" 
    for i in range(len(lst)): 
        lst[i] *= 2 
    return lst 

x = [1, 2, 3] 
modify_list(x) 
print(x)  # [2, 4, 6]

"""Prime numbers list comprehension.""" 

def is_prime(n):
    """Returns All the odd numbers > 1 that can be "/" by itself and 1."""
    if n < 2:           # Primes are >= 2
        return False
    for i in range(2, int(n**0.5) + 1): # we use n**0.5, so we don't check all the way up to n-1, which is wasteful. 
                                        # Example: For n = 97, you only check up to 10 instead of 96
        if n % i == 0:  # If divisible, it's not prime
            return False
    return True         # If no divisors found → prime

def prime_numbers(numbers): 
    """A Function that takes a list of integers and returns a list of the prime numbers."""
    # z = []
    return [n for n in numbers if is_prime(n)]
    # for n in numbers:
    #     if is_prime(n):  # Use the helper function
    #         z.append(n)  # Add to result list
    # return z

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(prime_numbers(numbers))  # Output: [2, 3, 5, 7]

"""1. For Loops & While Loop"""

FOR loop example: sum sales

sales = [1200, 900, 1450, 1800]
total_sales = 0

for s in sales:
    total_sales += s
print("Total Sales:",total_sales)  #5350



"""2.WHILE loop example: count down from"""

count = 5
while count > 0:
    print(count)
    count -= 1

# 5
# 4
# 3
# 2
# 1

"""while Loop — Basic Counter"""

# Print numbers from 1 to 10 (inclusive) using a while loop.
# Only print even numbers.
x = 1
while x <= 10:  # In a while loop, the condition needs to be a boolean expression, not x in range(1,11)
    if x % 2 == 0:
        print(x)
    x += 1
# 2
# 4
# 6
# 8
# 10

"""While Loop — Reverse Countdown"""
#Create a countdown from 10 to 1, but print "Blast Off!" instead of 0.

countdown = 10
while countdown > 0:
    print(countdown)
    countdown -= 1 
    if countdown == 0:
         print("Blast Off!")


def countdown_timer(start=10):
    """
    Counts down from 'start' to 1 and prints 'Blast Off!' at the end.
    """
    while start > 0:
        print(start)
        start -= 1
    print("Blast Off!")

countdown_timer()
    
"""3.While Loop — User Input"""
# Keep asking the user for a number until they type "stop".
    
user_input = ""
while user_input.lower() != "stop":
    user_input = input("Enter a number or 'stop' to quit: ") #converts whatever the user typed to lowercase — so "Stop"
    if user_input.isdigit(): # isdigit() checks if the string is made up of only digits (0–9). Also str.isnumeric(), isalpha() - Checks if all characters are letters.
        print(f"Double of your number is {int(user_input) * 2}")
        
# Example for negatives & decimals:  
    
def is_number(s):
    """Returns TRUE if a value is a number."""
    try:
        float(s)
        return True
    except ValueError:
        return False
n = is_number("12.34")
print(n)

"""4. FOR LOOP — List Processing"""
# Loop over this list and print names in uppercase.

names = ["Alice", "Bob", "Charlie"]

for name in names:
    print(name.upper())
    
# ALICE
# BOB
# CHARLIE

"""5. For Loop — Range"""
# Print all multiples of 4 between 1 and 30.

for n in range(1,30):
    if n % 4 == 0:
        print(n)
# 4
# 8
# 12
# 16
# 20
# 24
# 28

"""6. Function + For Loop"""
#Write a function that takes a list of numbers and returns the sum of squares.

n = [1,2,3,4,5,6,7,8,9]
def sum_of_squares(n):  
    """A function that returns SUM of squares via a list comprehension"""  
    return sum(i**2 for i in n)
print(sum_of_squares(n))



def sum_of_squares(numbers):
    """A function that returns SUM of squares via a for loop"""
    total = 0
    for n in numbers:
        total += n**2
    return total
print(sum_of_squares([1,2,3,4,5,6,7,8,9]))

"""7. Function + While Loop"""
# Write a function that asks for user input until they guess the number 7.

def guess_number():
    """A game of guessing the right number"""
    input_number = 0
    while input_number != 7:
        try:
            input_number = int(input("Please guess the number between 0-30 that is the number "))
            if input_number == 7:
                print("🎉 That is the correct number!")
                break
            elif input_number < 7:
                print("Too low! Try a higher number.")
            else:
                print("Too high! Try a lower number.") 
        except ValueError:
            print("Please enter a valid number.")
guess_number()
    
# Option 2:    
    
def guess_number():
    """Option 2 a game of guessing the right number"""
    while True:
        try:
            guess = int(input("Guess the number between 0 and 30: "))
            if guess == 7:
                print("🎉 That is the correct number!")
                break
            elif guess < 7: 
                print("Too low! Try a higher number.") #1️⃣ 
            else:
                print("Too high! Try a lower number.")  # 2️⃣ 
        except ValueError:
            print("Please enter a valid number.")
guess_number()

"""Using random.randint"""
import random

def guess_number():
    """Option 3 a game of guessing the right number"""    
    secret_number = random.randint(0, 30)  #1️⃣ random
    while True:
        try:
            guess = int(input("Guess the number between 0 and 30: "))
            if guess == secret_number:
                print("🎉 That is the correct number!")
                break
            elif guess < secret_number:
                print("Too low! Try a higher number.")
            else:
                print("Too high! Try a lower number.")
        except ValueError:
            print("Please enter a valid number.")

guess_number()

"""Including the count for quessing"""

def guess_number():
    """Option 4 a game of guessing the right number with Randomly generated number to guess each time"""
    secret_number = random.randint(0, 30)
    attempts = 0  #1️⃣ add counter
    
    while True:
        try:
            guess = int(input("Guess the number between 0 and 30: "))
            attempts += 1  # 2️⃣ increase guess count
            
            if guess == secret_number:
                print(f"🎉 Correct! You guessed it in {attempts} tries.")  # 3️⃣ show at the end
                break
            elif guess < secret_number:
                print("Too low! Try a higher number.")
            else:
                print("Too high! Try a lower number.")
        except ValueError:
            print("Please enter a valid number.")

guess_number()

"""8. Nested Loops"""
# Print a multiplication table for numbers 1–5.
# a multiplication table for the numbers 1 through 5, and separating each table with "---" as a divider.

for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i*j}")
    print("---")


"""10. Function with Parameters"""
# Write a function countdown(n) that uses a while loop to count down from n.
import time 
   
def countdown_timer(start=10): # defaults to 10 If no calling value is present
    """Counts down from 'start' to 1 and prints 'Blast Off!' at the end."""
    while start > 0:
        print(start)
        start -= 1
        time.sleep(1)  # wait for 1 second
    print("Blast Off!")

countdown_timer(6)


"""Division Try-except with a list of tuples"""

values = [(1, 0), (7, 9), (25, 9)] 
results = []

for numerator, denominator in values:
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        result = 0
    results.append(result)
    
print(results)

# --- only runs if script is executed directly ---
if __name__ == "__main__":
    guess_number()
