import random
import time
def main():
    print('''Can you guess how many heads will show up
            on flipping a coin 100 times?
            Using the number of heads that pop up at 40 and 70 flips,
            try to guess the number of heads at 100 flips!
            (Press enter to continue)''')

    input()

    flips = 0
    heads = 0

    while (flips < 100):
        oneflip = random.randint(0, 1)
        if (oneflip == 1):
            heads = heads + 1
        if (flips == 40):
            print('At 40 flips ' + str(heads) + ' showed up')
            time.sleep(2)
        if (flips == 70):
            print('At 70 flips ' + str(heads) + ' showed up')
            time.sleep(2)
        flips = flips + 1

    print('Enter your guess below:')

    guess = int(input())

    if (guess == heads):
        print('''WOAH! YOU HAD 1 IN 100 CHANCES AND YOU GOT THE NUMBER RIGHT!!!''')
    else:
        print('Nope :( Heads actually showed up ' + str(heads) + ' times')

playAgain = 'yes'

while (playAgain == 'yes' or 'y'):
    main()
    print('Do you want to play again')
    playAgain = input()
