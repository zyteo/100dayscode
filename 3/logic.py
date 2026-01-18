print(r'''
                         vv
                     vvv^^^^vvvvv
                 vvvvvvvvv^^vvvvvv^^vvvvv
        vvvvvvvvvvv^^^^^^^^^^^^^vvvvv^^^vvvvv
    vvvvvvv^^^^^^^^^vvv^^^^^^^vvvvvvvvvvv^^^vvv
  vvvv^^^^^^vvvvv^^^^^^^vv^^^^^^^vvvv^^^vvvvvv
 vv^^^^^^^^vvv^^^^^vv^^^^vvvvvvvvvvvv^^^^^^vv^
 vvv^^^^^vvvv^^^^^^vvvvv^^vvvvvvvvv^^^^^^vvvvv^
  vvvvvvvvvv^^^v^^^vvvvvv^^vvvvvvvvvv^^^vvvvvvvvv
   ^vv^^^vvvvvvv^^vvvvv^^^^^^^^vvvvvvvvv^^^^^^vvvvvv
     ^vvvvvvvvv^^^^vvvvvv^^^^^^vvvvvvvv^^^vvvvvvvvvv^v
        ^^^^^^vvvv^^vvvvv^vvvv^^^v^^^^^^vvvvvv^^^^vvvvv
 vvvv^^vvv^^^vvvvvvvvvv^vvvvv^vvvvvv^^^vvvvvvv^^vvvvv^
vvv^vvvvv^^vvvvvvv^^vvvvvvv^^vvvvv^v##vvv^vvvv^^vvvvv^v
 ^vvvvvv^^vvvvvvvv^vv^vvv^^^^^^_____##^^^vvvvvvvv^^^^
    ^^vvvvvvv^^vvvvvvvvvv^^^^/\@@@@@@\#vvvv^^^
         ^^vvvvvv^^^^^^vvvvv/__\@@@@@@\^vvvv^v
             ;^^vvvvvvvvvvv/____\@@@@@@\vvvvvvv
             ;      \_  ^\|[  -:] ||--| | _/^^
             ;        \   |[   :] ||_/| |/
             ;         \\ ||___:]______/
             ;          \   ;=; /
             ;           |  ;=;|
             ;          ()  ;=;|
            (()          || ;=;|
                        / / \;=;\
''')
print("Welcome to treasure island.\nYour mission is to find the treasure.")
direction=input("Do you want to go left or right?")
direction = direction.lower()
if direction == "left":
    action = input("Do you want to swim or wait?")
    action= action.lower()
    if action == "wait":
        colour = input("What colour door do you want to enter?")
        colour = colour.lower()
        if colour == "red":
            print("You were burned by fire. Game over")
            pass
        elif colour == "blue":
            print("You were eaten by beasts. Game over")
            pass
        elif colour == "yellow":
            print("You won!")
            pass
        else:
            print("You lost. Game over")
            pass
    elif action == "swim":
        print("You were attacked by a trout. Game over")
        pass
    else:
        print("Please enter either 'swim' or 'wait'. Game over.")
        pass
elif direction == "right":
    print("You fell into a hole. Game over.")
    pass
else:
    print("Please enter either 'left' or 'right'. Game over.")
    pass