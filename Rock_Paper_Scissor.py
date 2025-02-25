"""
WORKFLOW OF PROJECT:
1- Input from user(Rock, paper, scissor)
2- Computer choice (Computer will choose randomly not conditionally)
3- Result print

Cases:
A- Rock
Rock - Rock = tie
Rock - Paper = Paper win
Rock - scissor = Rock win

B- Paper
Paper - Paper = tie
Paper - Rock = Paper win
Paper - Scissor = Scissor win

C- Scissor
Scissor - Scissor = tie
Scissor - Rock = Rock win
Scissor - Paper = Scissor win

"""
"""
WORKFLOW OF PROJECT:
1- Input from user(Rock, paper, scissor)
2- Computer choice (Computer will choose randomly not conditionally)
3- Result print

Cases:
A- Rock
Rock - Rock = tie
Rock - Paper = Paper win
Rock - scissor = Rock win

B- Paper
Paper - Paper = tie
Paper - Rock = Paper win
Paper - Scissor = Scissor win

C- Scissor
Scissor - Scissor = tie
Scissor - Rock = Rock win
Scissor - Paper = Scissor win

"""
import random  # Importing the random module

item_list = ["Rock", "Paper", "Scissor"]  # List of possible choices

user_choice = input("Enter your move = Rock, Paper, Scissor= ").strip().upper()  # Taking and formatting user input
comp_choice = random.choice(item_list)  # Computer randomly selects a choice

print(f"User choice = {user_choice}, Computer choice = {comp_choice}")  # Displaying choices

if user_choice == comp_choice:  # Checking for a tie
    print("Both choose the same: = Match Tie")

elif user_choice == "Rock" or 'r':  # Checking user's rock choice
    if comp_choice == "Paper":
        print("Paper covers Rock = Computer Win")  # Paper beats rock
    else:
        print("Rock smashes Scissor = You win")  # Rock beats scissor

elif user_choice == "Paper" or 'p':  # Checking user's paper choice
    if comp_choice == "Scissor":
        print("Scissor cuts paper, Computer Win")  # Scissor beats paper
    else:
        print("Paper covers rock, You win")  # Paper beats rock

elif user_choice == "Scissor" or 's':  # Checking user's scissor choice
    if comp_choice == "Paper":
        print("Scissor cuts paper, You win")  # Scissor beats paper
    else:
        print("Rock smashes scissor, Computer win")  # Rock beats scissor

# Output : 
# Enter your move = Rock, Paper, Scissor= Scissor  
# User choice = SCISSOR, Computer choice = Paper  
# Scissor cuts paper, You win  

