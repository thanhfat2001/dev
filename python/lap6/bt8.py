'''
Bài 8: Guess the number
In this workbook, the user has to keep guessing a number until they get it right.
▪ Task 1
Store a "secret" number between 1 and 5. Then, prompt the user to enter a guess.
▪ Task 2
Set up a loop that keeps the user guessing until they get it right.
In other words, the loop should keep running while the guess is different from the secret.
▪ Task 3
After they guess the number, print:
You got it!

'''
from random import randint
number = randint(1,5)
print(f"The type of secrets number is: {number}")
print("I chose a number between 1 and 5. Try to guess it: ")
guess = int(input())

while (guess != number):
    print("Guess again: ")
    guess = int(input())

print("You got it!")