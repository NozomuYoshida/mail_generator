with open('./Input/Names/invited_names.txt') as file_names, open('./Input/Letters/starting_letter.txt') as file_letter:
    names = file_names.read().splitlines()
    print(names)
    starting_letter = file_letter.read()
    # print(starting_letter)
    for name in names:
        new_starting_letter = starting_letter.replace('[name]', name)
        # print(new_starting_letter)
        with open(f'./Output/ReadyToSend/letter_for_{name}.txt', 'w') as f:
            f.write(new_starting_letter)
