# Project 8

from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(text, shift, direction):
    if direction == "decode":
        shift *= -1
    caesar_message = ""
    for i in range(len(text)):
        if text[i] in alphabet:
            if alphabet.index(text[i]) + shift > len(alphabet)-1:
                caesar_message += alphabet[(alphabet.index(text[i]
                                                           ) + shift) - len(alphabet)]
            else:
                caesar_message += alphabet[alphabet.index(text[i])+shift]
        else:
            caesar_message += text[i]
    print(f"The message {direction} is {caesar_message}")


# TODO-1: Import and print the logo from art.py when the program starts.

print(logo)

# TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
# e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
# If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
# Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.

while True:
    direction = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt, or 'quit' to exit:\n")
    if direction == "quit":
        break
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
