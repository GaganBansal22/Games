from art import logo
import random,os

cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
def game():
    print(logo)
    gameOver=False
    wantCard=True
    userScore=0
    computerScore=0
    userCards=[]
    computerCards=[]
    c=random.choice(cards)
    userScore+=c
    userCards.append(c)
    c=random.choice(cards)
    computerScore+=c
    computerCards.append(c)
    c=random.choice(cards)
    userScore+=c
    userCards.append(c)
    
    print(f"Your cards: {userCards},Your score={userScore}")
    print(f"Computer's first card: {computerCards}")
    
    while not gameOver:
        wantCard=input("Do you want another card: ")
        if wantCard=="y":
            c=random.choice(cards)
            userScore+=c
            userCards.append(c)
        else:
            while computerScore<17:
                c=random.choice(cards)
                computerScore+=c
                computerCards.append(c)
        print(f"Your cards: {userCards}\nYour score={userScore}")
        print(f"Computer's cards: {computerCards}\nComputer's score={computerScore}")
        if userScore>21:
            print("You loose!")
            gameOver=True
        elif wantCard!="y":
            if computerScore>21 or userScore>computerScore:
                print("You Win!")
                gameOver=True
            elif computerScore==userScore:
                print("Draw!")
                gameOver=True
            else:
                print("You loose!")
                gameOver=True

game()
playAgain=input("Do you want to play again? ")
while playAgain=="y":
    os.system("cls")
    game()
    playAgain=input("Do you want to play again? ")
print("Goodbye")