import random

number = int(random.random() * 2)

if number == 0:
    print("heads")
elif number == 1:
    print("tails")
else:
    print("something went wrong")

fruits = ["apple","orange","pear"]
fruits.append("tomato")
print(fruits)
fruits.extend(["mango","strawberry"])
print(fruits)

friends=["A","B","C","D","E"]

randomiser = int(random.random() * len(friends))

print(friends[randomiser])

player_select = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors.\n"))

computer_select = int(random.random() * 3)

def player_win():
    print("You win")

def player_lose():
    print("You lose")

def player_draw():
    print("You draw")

def print_scissors():
    print('''
    
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')

def print_paper():
    print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

''')

def print_rock():
    print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

''')

def computer_choice(selection):
    print("Computer chose:\n")
    if selection == 0:
        print_rock()
    elif selection == 1:
        print_paper()
    elif selection == 2:
        print_scissors()
    else:
        print("error")

if player_select == 0:
    print_rock()
    if computer_select == 0:
        computer_choice(computer_select)
        player_draw()
    elif computer_select == 1:
        computer_choice(computer_select)
        player_lose()
    elif computer_select == 2:
        computer_choice(computer_select)
        player_win()
elif player_select == 1:
    print_paper()
    if computer_select == 0:
        computer_choice(computer_select)
        player_win()
    elif computer_select == 1:
        computer_choice(computer_select)
        player_draw()
    elif computer_select == 2:
        computer_choice(computer_select)
        player_lose()
elif player_select == 2:
    print_scissors()
    if computer_select == 0:
        computer_choice(computer_select)
        player_lose()
    elif computer_select == 1:
        computer_choice(computer_select)
        player_win()
    elif computer_select == 2:
        computer_choice(computer_select)
        player_draw()
else:
    print("error")

