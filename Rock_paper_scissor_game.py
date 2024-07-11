import random
lst=['r','p','s',]

chance=3
no_of_chance=0
computer_point=0
human_point=0

print("\t\t\t\t ROCK PAPER SCISSOR GAME \n\n\n")
print("r for Rock \np for Paper \ns for Scissor")

while no_of_chance < chance:
    inp=input("ROCK, PAPER, SCISSOR :")
    ran=random.choice(lst)

    if(inp == ran):
        print("DRAW 0 point each \n")

    elif(inp == "r" and ran == "p"):
        computer_point=computer_point+1
        print(f"Your guess {inp} and Computer guess is {ran} \n")
        print("Computer wins 1 point")
        print(f"Computer point is {computer_point} and Your point is {human_point}")

    elif(inp == "r" and ran == "s"):
        human_point=human_point+1
        print(f"Your guess {inp} and Computer guess is {ran} \n")
        print("You win 1 point")
        print(f"Computer point is {computer_point} and Your point is {human_point}")

    elif(inp == "p" and ran == "r"):
        human_point=human_point+1
        print(f"Your guess {inp} and Computer guess is {ran} \n")
        print("You win 1 point")
        print(f"Computer point is {computer_point} and Your point is {human_point}")

    elif(inp == "p" and ran == "s"):
        computer_point=computer_point+1
        print(f"Your guess {inp} and Computer guess is {ran} \n")
        print("Computer wins 1 point")
        print(f"Computer point is {computer_point} and Your point is {human_point}")

    elif(inp == "s" and ran == "r"):
        computer_point=computer_point+1
        print(f"Your guess {inp} and Computer guess is {ran} \n")
        print("Computer wins 1 point")
        print(f"Computer point is {computer_point} and Your point is {human_point}")

    elif(inp == "s" and ran == "p"):
        human_point=human_point+1
        print(f"Your guess {inp} and Computer guess is {ran} \n")
        print("You win 1 point")
        print(f"Computer point is {computer_point} and Your point is {human_point}")
    
    no_of_chance = no_of_chance + 1
    ch = chance - no_of_chance
    print(f"Number of chances left : {ch} \n")

print("GAME OVER")

if(human_point == computer_point):
    print("DRAW MATCH")

elif(human_point > computer_point):
    print("YOU WIN")
    
elif(human_point < computer_point):
    print("COMPUTER WIN")
