#This is a snake,gun,water game 
#Before run install the random module 
import random        #pip install random

# g for gun
# w for water
# s for snake

computer = random.choice([0, -1, 1])
youstr = input("Enter your choice (s, w, g): ").lower()  # Convert input to lowercase

youdict = {"s": 1, "w": -1, "g": 0}
reversedict = {1: "Snake", -1: "Water", 0: "Gun"} # Corrected reversedict

if youstr not in youdict:
    print("Invalid input. Please enter 's', 'w', or 'g'.")
else:
    you = youdict[youstr]

    print(f"Your choice: {reversedict[you]}\nComputer Choice: {reversedict[computer]}")

    if computer == you:
        print("Match Draw")
    elif (computer == -1 and you == 1) or (computer == 1 and you == 0) or (computer == 0 and you == -1):
        print("You Win!")
    elif (computer == -1 and you == 0) or (computer == 1 and you == -1) or (computer == 0 and you == 1):
        print("You Lose!")
    else:
        print("Something went wrong!") # This is unlikely to happen with the corrected logic
