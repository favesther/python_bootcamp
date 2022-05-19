#Step 5

import random

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]
import hangman_art as art, hangman_words as words
chosen_word = random.choice(words.word_list)
word_length = len(chosen_word)
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
print(art.logo)
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = ["_"] * len(chosen_word)
print(" ".join(display))

def end_of_game():
	if lives > 0:
		if "_" in display:
			return False
		else: return True
	else:		
		return True
tried = []	
while not end_of_game():
	guess = input("Guess a letter: ").lower()
	rightorwrong = False
	#Check guessed letter
	if guess in tried:
		print(f"\n--- You did '{guess}', try another! ---\n")
		if guess in display:
			rightorwrong = True
	else:
		for position in range(word_length):
			letter = chosen_word[position]
			# print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
			if letter == guess:
					display[position] = letter
					rightorwrong = True
					
		if not rightorwrong:
			lives -= 1
			print(f"\n-- Wrong, {guess} not in the target word, you lose 1 point. You have {lives} points left. --\n")
			print(art.stages[lives])
		else:
			print("\nYou are correct.\n")
			print(" ".join(display),"\n")
			
	tried.append(guess)
	

if lives > 0:
	print(f"{art.congrats} \n You win!")
else:
	print("You lose...")