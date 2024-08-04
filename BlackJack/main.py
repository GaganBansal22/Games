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

    if userScore > 21:
        userScore = userScore - 10
    # accounting for two aces being pulled from the deck
    
    print(f"Your cards: {userCards},Your score={userScore}")
    print(f"Computer's first card: {computerCards}")
    
    while not gameOver:
        wantCard=input("Do you want another card: ")
        if wantCard==("y" or "yes"):
            c=random.choice(cards)
            userScore+=c
            userCards.append(c)

            if userScore > 21:
                numberOfCards = len(userCards)
                i = 0
                while userScore > 21 and i < numberOfCards:
                    if userCards[i] == 11:
                        userCards[i] = 1
                        userScore = userScore - 10
                    i += 1
            # checking to see if the player has an ace and has a score greater than 21

        elif computerScore > userScore:
            gameOver = True
        
        while computerScore < userScore and userScore <= 21:
            c=random.choice(cards)
            computerScore+=c
            computerCards.append(c)
        
        print(f"Your cards: {userCards}\nYour score={userScore}")
        print(f"Computer's cards: {computerCards}\nComputer's score={computerScore}")
        if userScore>21:
            print("You lose!")
            gameOver=True
        elif wantCard!=("y" or "yes"):
            if computerScore>21 or userScore>computerScore:
                print("You Win!")
                gameOver=True
            elif computerScore==userScore:
                print("Draw!")
                gameOver=True
            else:
                print("You lose!")
                gameOver=True

game()
playAgain=input("Do you want to play again? ")
while playAgain==("y" or "yes"):
    os.system("cls")
    game()
    playAgain=input("Do you want to play again? ")
print("Goodbye")
