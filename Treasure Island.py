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
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction = input("Choose a direction you want to go. Pick Left or Right? ").lower()
if direction == "left":
    print("You are getting closer to your goal")

    direction = input("You reach another crossroad. The three doors are across the lake. You are a world class swimmer. Do you swim"
          " across or do you wait? Pick Swim or Wait ").lower()

    if direction == "wait":
        print("The lake splits in two like the Red Sea, giving you an easy way to cross and reach the final three doors"
              " toward your goal.")
        print("The Treasure is within reach.")

        direction = input("You approach three doors, all aglow with a different color each. One red, One Yellow, One Blue."
                          " What do you choose? ").lower()
        if direction == "yellow":
            print("You win!!!!!!")

        elif direction == "red":
            print("The door opens and engulfs you in flames and sulfur.\nGAME OVER")
        elif direction == "blue":
            print("Shadow Beasts reach through the open blue door, grab you"
                  " and pull you into everlasting oblivion.\nGAME OVER")

    else:
        print("Two portals open up. Out of one, The Leviathan appears and carries you off into the dark"
              "ness through the other.\nGAME OVER")


else:
    print("You fell into a hole.\nGAME OVER")