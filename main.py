PLACEHOLDER = "[name]"


names = []
with open("Input/Names/invited_names.txt") as content:
    for item in content:
        names.append(item.split('\n')[0])

letter = ""
with open("Input/Letters/starting_letter.txt") as content:
    letter = content.read()


for name in names:
    with open(f"Output/ReadyToSend/letter_for_{name}.txt", "w") as data:
        data.write(letter.replace(PLACEHOLDER, f"{name}"))