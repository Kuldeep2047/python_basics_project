import random
from tabulate import tabulate
print("-----------WELCOME TO GAME------------")

#Make table for difficulty of game
def game_level():
    print("\n           Choose Game Level         ")
    header=['S.No.','Game Level','Number Range']
    data=[['1 ','Easy','1 to 5'],['2 ','Medium','1 to 10'],['3 ','Hard','1 to 50']]
    print(tabulate(data, headers=header,tablefmt='fancy_grid'))
    level=int(input("Choose your Game level(1,2,3) :"))
    return level

#Function to check user guessing number is correct or not
def guess_number():
    a=game_level()
    Data=[]
    if a==1:
        i=1
        c1=c2=0
        while i<=3:
            c_input=random.randint(1,5)
            user_input=int(input(f"{i}. Guess any number you want between 1 to 5 :"))
            if c_input==user_input:
                b="Pass"
                c1+=1
            else:
                b="Fail"
                c2+=1
            input_=[i,user_input,c_input,b]
            Data.append(input_)
            i+=1
        return Data,c1,c2
    elif a==2:
        i=1
        c1=c2=0
        while i<=3:
            c_input=random.randint(1,10)
            user_input=int(input(f"{i}. Guess any number you want between 1 to 10 :"))
            if c_input==user_input:
                b="Pass"
                c1+=1
            else:
                b="Fail"
                c2+=1
            input_=[i,user_input,c_input,b]
            Data.append(input_)
            i+=1
        return Data,c1,c2
    elif a==3:
        i=1
        c1=c2=0
        while i<=3:
            c_input=random.randint(1,50)
            user_input=int(input(f"{i}. Guess any number you want between 1 to 50 :"))
            if c_input==user_input:
                b="Pass"
                c1+=1
            else:
                b="Fail"
                c2+=1
            input_=[i,user_input,c_input,b]
            Data.append(input_)
            i+=1
        return Data,c1,c2
      
# function for print the output in the form of Table
def output(Table,C,D):
    header=['S.No.','User_Input','Target_Value','Result']
    print(tabulate(Table, headers=header,tablefmt='fancy_grid'))
    if C>D:
        print("CONGRATULATION!! YOU WIN THE GAME")
    else:
        print("You've lost the game.\nTRY AGAIN!")
    print("------------------------------")
    
Data_out,A,B=guess_number()

output(Data_out,A,B)    


#check the condition for more playing or exit the game
while True:
    choice=input("Play more (Press Y or y) or Exit game(Press N or n) :")
    if choice=='N' or choice=='n':
        print("------------------------------")
        print("THANKS FOR PLAYING THIS GAME")
        print("------------------------------")
        break
    Data_out,A,B=guess_number()
    output(Data_out,A,B)
    