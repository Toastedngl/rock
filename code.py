import random

options = ["Rock", "Paper", "Scissors"]
computer_choice = random.choice(options)


player_choice = input("rock, paper, or scissors?").lower()

print (f"The computer chose : {computer_choice}!")

if player_choice == ("rock") and computer_choice == ("paper"):

  print (f"Computer wins!")

elif player_choice == ("rock") and computer_choice == ("scissors"):

  print (f"Player wins!")

elif player_choice == ("scissors") and computer_choice == ("paper"):

  print (f"Player wins!")

elif player_choice == ("scissors") and computer_choice == ("rock"):

  print (f"Computer wins!")

elif player_choice == ("paper") and computer_choice == ("rock"):

  print (f"Player wins!")

elif player_choice == ("paper") and computer_choice == ("scissors"):

  print (f"Computer wins!")

else:

  print (f"It's a tie!")
