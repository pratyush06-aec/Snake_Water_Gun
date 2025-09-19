import random

computer_choice= random.choice([0, -1, 1])

a= str(input("Enter your name: "))

if a.isnumeric():
    raise ValueError("Your name can't be in numeric format or have digits in it. Try again next time!!!")
else:
    print(f"Welcome to this game {a}!!!")

    try:
        you_dict= {"Snake":0, "Gun":1, "Water":-1}
        reverse_you_dict= {0:"Snake", 1:"Gun", -1:"Water"}

        you= input("Enter your choice: ")
        your_choice= you_dict[you]

        print(f"You choose {reverse_you_dict[your_choice]}\nComputer choose {reverse_you_dict[computer_choice]}")


        if(computer_choice==your_choice):
            print("It's a draw!!!")

        else:
            if(computer_choice==1 and your_choice==0):
                print("Computer won!!!!")

            elif(computer_choice==1 and your_choice==-1):
                print("You won!!!")

            elif(computer_choice==0 and your_choice==1):
                print("You won!!!")

            elif(computer_choice==0 and your_choice==-1):
                print("Computer won!!!")

            elif(computer_choice==-1 and your_choice== 0):
                print("You won!!!")

            elif(computer_choice==-1 and your_choice==1):
                print("Computer won!!!")

            else:
                print("Something went wrong!!!")

    except KeyError as k:
        print(f"Hey {a}, you have raised a key-error. Better luck next time!!!!")
