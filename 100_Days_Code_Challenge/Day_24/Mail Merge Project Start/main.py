#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


file = open("Input/Names/invited_names.txt")

list = file.readlines()
file.close()

new_list = []
for name in list:
    new_list.append(name.strip())

for name in new_list:
    with open("Input/Letters/starting_letter.txt") as file:
        letter = file.read()
        letter = letter.replace("[name]", name)
        with open(f"Output/ReadyToSend/letter_for_{name}.txt", mode="w") as new_file:
            new_file.write(letter)
