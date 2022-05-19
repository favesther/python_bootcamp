import caesar_cipher_art as art
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def cal(a, b, direction):
	import numpy as np
	if direction == "encode":
		return np.add(a,b)
	if direction == "decode":
		return np.subtract(a,b)
		
def caesar(text, shift, direction):

	output = []
	if direction in ["encode","decode"]:
		for t in text:
			if t in alphabet:
				output_index = cal(alphabet.index(t), shift%26, direction)
				if output_index not in range(-len(alphabet)+1, len(alphabet)):
					output_index = abs(len(alphabet) - output_index)
				output.append(alphabet[output_index])
			else:
				output.append(t)
	else:
		output.append("Invalid Input.")
	print(f"The {direction}d text is: {''.join(output)}.")
	
def cipher():
	direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\t")
	text = input("Type your message:\t").lower()
	shift = int(input("Type the shift number:\t"))

	caesar(text, shift, direction)

cipher()
restart = input("Do you want to go over again? Y/N\t")

while restart not in ["Y","N"]:
	restart = input("Wrong Input!\nDo you want to go over again? Y/N\t")

while restart == "Y":
	cipher()
	restart = input("Do you want to go over again? Y/N\t")
	
if restart == "N": print("Goodbye")