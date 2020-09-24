import random

guessesTaken = 0

print("Hello! What thy name be?")

name = input()
print("Well, " + name + ", I'm thinking of a secret number between 1 and 20.")
print("Take a guess. You have 6 tries.")
number = random.randint(1, 20)

for guessesTaken in range(6):
    guess = int(input())
    if (guess > number):
        print("Your guess is too high")
    elif (guess < number):
        print("Your guess is too low")
    else:
        break

if (guess == number):
    print("Good job, " + name + "! You guessed the right number in " + str(guessesTaken+1) + " tries.")
else:
    print("Nope, the number I had in mind was " + str(number))

print("Game over.")
