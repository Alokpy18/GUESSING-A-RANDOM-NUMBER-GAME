# generate a random integer between 1 and 100:
import random
jackpot = random.randint(1, 100)

guess = int(input("guess the number"))
counter = 1
while guess != jackpot:
    if guess < jackpot:
        print("wrong! guess higher")
    else:
        print("wrong! guess lower")
    guess = int(input("guess the number"))
    counter += 1
    
print("congratulations! correct guess")
print("attempts", counter) 
