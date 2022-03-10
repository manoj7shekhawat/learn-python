

with open("./Input/Names/invited_names.txt", mode="r") as fn:
    for x in fn:
        # Removing trailing new line char \n
        name = x.rstrip()

        with open("./Input/Letters/starting_letter.txt", mode="r") as fsl:
            text = fsl.read()
            text = text.replace("[name]", name)
            #print(f"{text}")

        with open("./Output/ReadyToSend/letter_for_" + name + ".txt", mode="w") as fhL:
            fhL.write(text)


print("Done :-)")