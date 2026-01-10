with open("./Input/Letters/starting_letter.txt", mode="r") as letter:
    template = letter.read()

#Creating a list of all names and replacing it one by one in place of "[name]".
with open("./Input/Names/invited_names.txt", mode="r") as names:
    for line in names:
        name = line.strip()
        personalized_letter = template.replace("[name]", name)
        with open(f"./Output/ReadyToSend/letter_to_{name}.txt", mode="w") as invite:
            invite.write(personalized_letter)