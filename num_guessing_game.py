import random

number= random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print(number)
guess=int(input("Guess a number between 1 and 100: "))
attempt=1
if guess== number:
    print("Your guess is correct.")
else:
    while guess != number:
        if guess<number:
            print("Too Low!!! Try Again.\n")
            
        elif guess > number:
            print("Too High!! Try again.\n")
            
        guess=int(input('Guess Again:'))    
        attempt+=1
print("You guessed correct in attempts: ",attempt)