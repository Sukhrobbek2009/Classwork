import random
import time
print("Dice game")
print("- - - Welcome to Dice game - - - ")
print("Get ready.....")
for i in range (3, 0, -1):
    print(i)
    time.sleep(2)
print("GO")

player1_score = 0
player2_score = 0
rounds = int(input("How many rounds do you want to play?"))

for i in range(1, rounds + 1):
    print("\n - - -Round {i} - - -")

    input("Player 1 , press Enter to roll the dice ")
    roll = random.randit(1, 6)
    print("Player 1 rolled: ", roll)
    player1_score += roll
    input("Player 2, press Enter to roll the dice ")
    roll2= random.randint(1, 6)
    print("Player 2 roled: ", roll2)
    player2_score += roll2

print('\n Final Score')
print("Player 1's total score : ", player1_score)
print("Player 2's total score : ", player2_score)

if player1_score > player2_score:
    print("Player 1 wins")
elif player2_score > player1_score:
    print("Player 2 wins")
else:
    print("It's a tie")
    