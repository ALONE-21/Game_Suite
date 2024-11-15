import os
import time
import random

def main_menu(wallet):
    clearConsole()
    print(" welcome to slot machine game! ")
    print(" 1. Slot game \n 2. Withdraw money \n 3. Deposite money ")
    print("Wallet: $", wallet)
    game = int(input("\nPlease Select your choice: "))

    if game == 1:
        slots(wallet)
    elif game == 2:
        withdrawFunds(wallet)
    elif game== 3:
        depositFunds(wallet)
    
def clearConsole():
	command = 'clear'
	if os.name in ('nt','dos'):
		command = 'cls'
	os.system(command)

#Shows the current wallet
def showWallet(wallet):
	print("\nWallet: $", wallet , "\n")

#Shows to bet 0 to go to main menu
def showTip():
	print("\n----[Useful Tip]----")
	print("\nTo go back at the main menu at any given time, press the right shift key.")

#Checks whether the bet was over the wallet amount
def betCheck(wallet, bet):

	if bet == 0:
		main_menu(wallet)
	
	if wallet == 0:
		print("Sorry! Not enough funds!")
		time.sleep(3)
		main_menu(wallet)

	if bet > wallet:
		print("Not enough funds for that bet!")
		time.sleep(1.4)
		main_menu(wallet)

#Deposit new funds into wallet
def depositFunds(wallet):

	clearConsole()

	print("----[Deposit Funds]----\n")
	deposit = int(input("How much would you like to deposit?: $"))

	wallet += deposit

	print("Succesfully updated wallet with: $", deposit)
	time.sleep(2)

	main_menu(wallet)

#Withdraw funds from wallet
def withdrawFunds(wallet):

	clearConsole()
	print("----[Withdraw Funds]----\n")
	withdrawal = int(input("How much would you like to withdraw?: $"))

	wallet -= withdrawal

	print("Succesfully withdrawed: $", withdrawal)
	time.sleep(2)
	main_menu(wallet)

def slots(wallet):

	clearConsole()

	print("====[Welcome to Slots!]====\n")
	

	print("[1] Tycoon Maniya\n")
	print("[2] Fire Joker\n")
	print("[3] Sweet Bonanza\n")

	slot_choice = input("Please select your game: ")

	if slot_choice == "1":
		tycoon(wallet)
	elif slot_choice == "2":
		fire_joker(wallet)
	elif slot_choice == "3":
		sweet_bonanza(wallet)
	else:
		main_menu(wallet)

def tycoon(wallet):

	clearConsole()
	

	pepper = ['Black Pepper', 'Red Pepper', 'Green Pepper']
	lemon = ['Black lemon', 'Red lemon', 'Green lemon']
	apple = ['Black apple', 'Red apple', 'Green apple']

	# random_pepper = random.choice(pepper)
	# random_lemon = random.choice(lemon)
	# random_apple = random.choice(apple)

	print("----[Now playing Tycoon Manya]----")

	showWallet(wallet)
	bet = int(input("\nPlease place your bets [Minimum $10]: "))

	betCheck(wallet, bet)
	
	winnings = bet * 250	

	winner = "<JACKPOT> Congratulations! You won:" , "$" , winnings
	
	for i in range(8):
		random_pepper = random.choice(pepper)
		random_lemon = random.choice(lemon)
		random_apple = random.choice(apple)
		print("| " + random_pepper + " | " + random_lemon + " | " + random_apple)
		time.sleep(0.8)

		if random_pepper.startswith("Black") & random_apple.startswith("Black") & random_lemon.startswith("Black"):
			print(winner)
			wallet += winnings
			time.sleep(3) 
			tycoon(wallet)
		elif random_pepper.startswith("Red") & random_apple.startswith("Red") & random_lemon.startswith("Red"):
			print(winner)
			wallet += winnings
			time.sleep(3)
			tycoon(wallet)
		elif random_pepper.startswith("Green") & random_apple.startswith("Green") & random_lemon.startswith("Green"):
			print(winner)
			wallet += winnings
			time.sleep(3)
			tycoon(wallet)
	
	print("To bad! You lost!")
	wallet -= bet
	time.sleep(3)	

	tycoon(wallet)

	return wallet

#Sweet bonanza slot machine game
def sweet_bonanza(wallet):
		clearConsole()
		lane1 = ['Bonus Bomb','Grapes','Banana','Lemon','Pear','Strawberry']
		lane2 = ['Bonus Bomb','Grapes','Banana','Lemon','Pear','Strawberry']
		lane3 = ['Bonus Bomb','Grapes','Banana','Lemon','Pear','Strawberry']
		print("----[Now playing Sweet Bonanza]----\n")
		
		showWallet(wallet)
		bet = int(input("\nPlease place your bets: $"))

		betCheck(wallet, bet)

		for i in lane1:

			random_lane1 = random.choice(lane1)
			random_lane2 = random.choice(lane2)
			random_lane3 = random.choice(lane3)

			multipliers = ['5','10','25','50','100']

			print("| " + random_lane1 + " | " + random_lane2 + " | " + random_lane3 + " | ")
			time.sleep(0.2)

			if random_lane1.startswith("Bonus Bomb") & random_lane2.startswith("Bonus Bomb") & random_lane3.startswith("Bonus Bomb"):
				bbm = random.choice(multipliers)
				bbmPlusBet = int(bbm) * bet
				wallet += bbmPlusBet
				print("Congratulations: $",bbmPlusBet)
				time.sleep(3)
				sweet_bonanza(wallet)
			elif random_lane1.startswith("Bonus Bomb") & random_lane2.startswith("Bonus Bomb"):				
				bbm = random.choice(multipliers)
				bbmPlusBet = int(bbm) * bet
				wallet += bbmPlusBet
				print("Congratulations: $",bbmPlusBet)
				sweet_bonanza(wallet)
			elif random_lane1.startswith("Bonus Bomb") & random_lane3.startswith("Bonus Bomb"):
				bbm = random.choice(multipliers)
				bbmPlusBet = int(bbm) * bet
				wallet += bbmPlusBet
				print("Congratulations: $",bbmPlusBet)
				time.sleep(3)
				sweet_bonanza(wallet)
			elif random_lane2.startswith("Bonus Bomb") & random_lane3.startswith("Bonus Bomb"):
				bbm = random.choice(multipliers)
				bbmPlusBet = int(bbm) * bet
				wallet += bbmPlusBet
				print("Congratulations: $",bbmPlusBet)
				time.sleep(3)
				sweet_bonanza(wallet)
				print("Too bad! You lost!")
				wallet += int(bbmPlusBet)
				time.sleep(1.5)
		
		wallet -= bet
		sweet_bonanza(wallet)

		return wallet

def first_menu():
	clearConsole()
	print("----[Welcome to Casino Royale]----\n")
	wallet = int(input("Please deposit funds: $"))
	errorHandling(wallet)
	main_menu(wallet)

#Check if int
def errorHandling(arg1, arg2="", arg3="", arg4=""):
	if isinstance(arg1, int):
		pass
	else:
		usage()

#Restarts scripts when input is not a int
def usage():
	print(" Please use an integer! ")
	time.sleep(1.3)
 
def fire_joker(wallet):

	clearConsole()

	lane1 = ['Fire Joker','Grapes','Banana','Lemon','Pear','Strawberry']
	lane2 = ['Fire Joker','Grapes','Banana','Lemon','Pear','Strawberry']
	lane3 = ['Fire Joker','Grapes','Banana','Lemon','Pear','Strawberry']

	random_lane1 = random.choice(lane1)
	random_lane2 = random.choice(lane2)
	random_lane3 = random.choice(lane3)

	print("----[Now playing Fire Joker]----\n")

	print("If you bet 0, you'll return to the main menu\n")

	showWallet(wallet)
	bet = int(input("\nPlease place your bet: $"))
	
	betCheck(wallet, bet)
	winning_jackpot = bet * 12300
	winning1 = bet * 12
	
	winner = "Congratulations! You won: $", winning1

	jackpot = "[JACKPOT] CONGRATULATIONS! YOU WON THE JACKPOT! You could've won: $",winning_jackpot

	for i in lane1:

		random_lane1 = random.choice(lane1)
		random_lane2 = random.choice(lane2)
		random_lane3 = random.choice(lane3)

		print("| " + random_lane1 + " | " + random_lane2 + " | " + random_lane3 + " | ")
		time.sleep(0.2)

		if random_lane1.startswith("Fire Joker") & random_lane2.startswith("Fire Joker") & random_lane3.startswith("Fire Joker"):
			print(jackpot)
			wallet += winning_jackpot
			time.sleep(5)
			fire_joker(wallet)
		elif random_lane1.startswith("Fire Joker") & random_lane2.startswith("Fire Joker"):
			print(winner)
			wallet += winning1
			time.sleep(5)
			fire_joker(wallet)
		elif random_lane1.startswith("Fire Joker") & random_lane3.startswith("Fire Joker"):
			print(winner)
			wallet += winning1
			time.sleep(5)
			fire_joker(wallet)
		elif random_lane2.startswith("Fire Joker") & random_lane3.startswith("Fire Joker"):
			print(winner)
			wallet += winning1
			time.sleep(5)
			fire_joker(wallet)

	print("You lost! Too bad.")
	wallet -= bet
	time.sleep(2)
	fire_joker(wallet)

	return wallet
first_menu()