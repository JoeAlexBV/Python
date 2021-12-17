import random


def _roll_dice(counter):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    counter += 1
    while dice1 != 6 or dice2 != 6:
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        counter += 1
    return counter


print(
    """
     __________________________
    |                          |
    |   Double Six Dice Game   |
    |__________________________|
    """
)

player1 = input("Player 1 enter your name:")
counter1 = _roll_dice(0)
print(f"You rolled: {counter1} times")

player2 = input("Player 2 enter your name:")
counter2 = _roll_dice(0)
print(f"You rolled: {counter2} times")

if counter1 > counter2:
    print(f"{player2} Wins!")
elif counter2 > counter1:
    print(f"{player1} Wins!")
else:
    print("Draw Game!")
