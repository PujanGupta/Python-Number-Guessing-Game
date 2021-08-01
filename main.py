import random


number = random.randint(0, 101)
tries = 0
found = False

while found != True:
    guess = int(input("Guess: "))
    tries += 1
    
    if guess > number:
        print("Your guess is greater than what I am thinking of")
    if guess < number:
        print("Your guess is less than the number I am thinking of")
    if guess == number:
        found = True
        print(f"You guessed in {tries} number of guesses")
            
            
    