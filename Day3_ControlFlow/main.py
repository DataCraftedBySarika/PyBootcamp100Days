print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
LR = input("You\'re at a crossroad, where do you want to go? Type Left or Right\n").title()
if LR == "Left":
    SW = input("You\'ve come to a lake.There is an island in the middle of the lake.\nType Wait to wait for a boat.\n"
               "Type swim to swim across.\n").title()
    if SW == "Wait":
        Door = input("Which Door Red, Yellow,Blue?").title()
        if Door == "Red":
            print("Oops It's a room full of fire.Game Over!")
        elif Door == "Yellow":
            print("Congratulations, you found the treasure.\n Hurrah You Win!")
        elif Door == "Blue":
            print("Oops, you enter a room of beasts Game Over!")
        else:
            print("Invalid Door")

    else:
        print("Oops, you got attacked by an angry trout. Game Over!!")

else:
    print("Oops,you fell in to a hole. Game Over!!")
