# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

name_file = open(
    "Input/Names/invited_names.txt", 'r')
names = [name.rstrip() for name in name_file.readlines()]
name_file.close()

for name in names:
    letter = open("Input/Letters/starting_letter.txt", 'r')
    new_letter = open(f"Output/ReadyToSend/letter_for_{name}.txt", 'w')
    for line in letter.readlines():
        line = line.replace("[name]", name)
        new_letter.write(line)
    new_letter.close()
