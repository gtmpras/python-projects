#input two users:player1 and player2
pl1=input("Enter player1 name: \n")
pl_2=input("Enter player2 name: \n")
#player 1:input multidigit numbers

import getpass#number hiding module

inp1=int(input("How many digits you wants to enter? "))
inp1_str=getpass.getpass("Enter the digit:")#hiding the inputed number
inp2=int(inp1_str)#converting string form into integer

if inp1==len(str(inp1_str)):# Is no_of digits = lengths of digits process:

#player 2 :guess the number

    guess=int(input("Guess the number entered by player1: "))
    #if: player2 guess corrects he considerd as mastermind
   
    i=1
    for i in range(4):  
        if(guess>inp2):
            print("Entered number is greater.")

        elif(guess==inp2):
            print(f'Congratulations {pl_2} you are mastermind.')
            break

        else:
            print("Entered number is smaller.")
            #if guess is incorrect then reveal some of the digits.
            #if player 2 corrects some numbers that are correct player 1 reveals those numbers as a hint \
        for j in str(inp1_str):
            for k in str(guess): 
                if j==k :
                    print("Your corect digit is: ",j)
                    print("\n")
        guess=int(input("Enter your guess again: "))

    #if guess correct or till chances becomes 0
    #if player 2 can't guess then player 1 wins
    if(guess!=inp2):
        print(f"Opps! you couldn't guess until 5 chances, Winner is  {pl1} and number is:",inp1_str)
  
else:
    print("You didn't entered the specific size of digits.")