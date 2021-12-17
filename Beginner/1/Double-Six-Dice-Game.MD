In this challenge, we will use a step by step approach to create a 2-player dice game with the following rules:

The first player rolls a pair of dice, and keeps rolling the dice again and again, until they roll a double six.
It is then the turn of the the second player. They too will roll the dice and keep doing so until they roll a double six.
The winner of the game is the user who rolled a double six in the smaller number of attempts.
The game ends on a draw if both players used the same number of attempts to roll a double six.

# Step 1: Displaying a welcome banner
Write some Python code using the print command to display to display a nice banner with the title of the game: “Double Six Dice Game”. Your banner could look like this:
 __________________________
|                          |
|   Double Six Dice Game   |
|__________________________|

# Step 2: Retrieving the name of the first player
Use an input command to ask for the first player to enter their name. Store this name in a variable called player1. You will have to use this variable later on, at the end of the game to display the name of the winner of the game.

# Step 3: Throwing the first dice…
Use the randint function from the random library to generate and output a random number between 1 and 6 for the first dice. Store this randomly generated number in a variable called dice1.

# Step 4: Throwing the second dice…
Re-use the code from step 3 to generate and output a second random number between 1 and 6. Store this randomly generated number in a variable called dice2.

# Step 5: Carry on throwing the dice until a double six is rolled.
You will now need to use a while loop, to repeat steps 3 and 4 for as long as player 1 does know throw a double six.

# Step 6: Counting the number of throws.
Add a counter using a variable called counter1 to count the number of attempts/throws of the the dice. You will need to:
* Initialise your counter1 variable at the start of the game to 0.
* Increment your counter1 variable by 1 after each throw of the two dice.
* Output the total number of attempts once a double six has been rolled.

# Step 7: Player 2’s turn…
Repeat steps 2 to 6 for player 2!

# Step 8: Deciding who wins the game!
Compare the counter of both players to display the appropriate message to end the game:
* Player 1 wins if they have had less attempts than player 2.
* Player 2 wins if they have had less attempts than player 1.
* The game ends on a draw if both players have had exactly the same number of attempts to roll a double six.