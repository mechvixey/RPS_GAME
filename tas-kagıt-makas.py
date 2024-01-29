import random
list=["rock","paper","scissors"]
ask=int(input("How many times do you want to play?"))
player_score=0
computer_score=0
count=0
while count<ask:
    plyr=input("rock\npaper\nscissors\nWhat is your answer? ")
    if plyr not in list:
        print("Invalid answer. Please try again.")
        continue
    comp=random.choice(list)
    
    if plyr=="rock" and comp=="scissors":
        player_score +=1
    elif comp=="rock" and plyr=="scissors":
        computer_score+=1
    elif plyr=="paper" and comp=="rock":
        player_score += 1
    elif comp=="paper" and plyr=="rock":
        computer_score+=1
    elif plyr=="scissors" and comp== "paper":
        player_score += 1
    elif comp=="scissors" and plyr== "paper":
        computer_score+=1
    print(f"The answer of computer is:{comp}")

    count +=1
if player_score>computer_score:
    print("You win!Congratulations.")
elif player_score==computer_score:
    print("You drew.")
else:
    print("You lost")
print(f"Your total score is {player_score}.")


