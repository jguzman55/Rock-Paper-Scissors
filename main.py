import random 
print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

imgs = [rock, paper, scissors]

print('What do you choose?')

choice = int(input("Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))



if choice >= 3 or choice < 0:
  print("Invalid input. You lose!")
else:  
  print('You chose:')
  print(imgs[choice])

  ran = random.randint(0, 2)
  print('Computer chose:')
  print(imgs[ran])


  if choice == 0 and ran == 2:
    print('You win!')
  elif ran == 0 and choice == 2:
    print('You lose!')
  elif ran > choice:
    print('You lose!')
  elif choice > ran:
    print('You win!')
  elif ran == choice:
    print('It is a draw!')
