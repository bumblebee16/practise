from random import randint

choices = ["Rock", "Paper", "Scissors"] # universal list of choices available

while True:
	print("Welcome to play Rock, Paper and Scissors \n")
	print("There are two players. One is you, the other one is the computer. \n")
	print("Enter your choice as the entire character \n")
	player_choice = int(input("Rock(0), Paper(1) or Scissors(2)? ")) # player choice
	if(player_choice != 0 and player_choice != 1 and player_choice != 2):
		print("Wrong choice. Please enter amongst available options")
		continue
	computer_choice = randint(0,2) # random choice for computer
	# logic for comparison
	# rock-paper:paper,rock-scissors:rock
	# paper-scissors:scissors
	choice_score = player_choice - computer_choice
	if choice_score == 0:
		print("Its a tie! You chose " + choices[player_choice] + " and the computer chose " + choices[computer_choice])
	elif choice_score == -1 or choice_score == 2:
		print("You lose! :( You chose " + choices[player_choice] + " and the computer chose " + choices[computer_choice])
	else:
		print("Hurray! You win! You chose " + choices[player_choice] + " and the computer chose " + choices[computer_choice])
	# option to check if the player wants to continue playing
	print("\n Now \n")
	menu = int(input("Still want to continue playing? yes = 1, no = 2 : ")) 
	if menu == 1:
		continue
	elif menu == 2:
		break
	else:
		print("Invalid option. Exiting game.")

# program ends here
print("Thanks for playing!")