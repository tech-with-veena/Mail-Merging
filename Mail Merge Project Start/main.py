placeholder="[name]"
with open("./Input/Names/invited_names.txt") as namesfile:
    names=namesfile.readlines()
    print(names)
with open("./input/letters/starting_letter.txt") as letters:
    letterfile=letters.read()
    for name in names:
        stripname=name.strip()
        newname=letterfile.replace(placeholder,stripname)
        with open(f"./Output/ReadyToSend/letter_for_{stripname}.txt",mode="w") as completedfile:
            completedfile.write(newname)


