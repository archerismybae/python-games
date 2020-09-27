import random
import time

def main():
    print('''You are a wandering sorcerer looking for the anient treasures of Merlin.
    After years of searching you finally reach the castle believed to be
    Merlin's own handiwork. However, there are two entrances. One holds the treasure,
    where as the other houses a dragon. Which entrance do you enter through? (1 or 2)''')
    number = input()
    print('You approach the entrance...')
    time.sleep(2)
    print('It is quiet and dark..')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws...')
    time.sleep(2)
    realEntrance = random.randint(1, 2)
    if number == str(realEntrance):
        print('..and hands you the treasure!')
    else:
        print('..and gobbles you down in one bit!')


playAgain = 'yes'
while (playAgain == 'yes' or playAgain == 'y'):
    main()
    print('Do you want to play again? (yes or no)')
    playAgain = input()