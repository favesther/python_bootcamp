PLACEHOLDER = "[name]"

with open('/Users/yuyuezhu/Documents/GitHub/python_bootcamp/Mail Merge Project Start/Input/Letters/starting_letter.txt') as letter:
    letter_sample = letter.read()

with open('/Users/yuyuezhu/Documents/GitHub/python_bootcamp/Mail Merge Project Start/Input/Names/invited_names.txt') as names:
    names_list = names.read().split()
    # names_list = names.readlines()
    for name in names_list:
            new_letter = letter_sample.replace(PLACEHOLDER, name)
            with open(f'/Users/yuyuezhu/Documents/GitHub/python_bootcamp/Mail Merge Project Start/Output/ReadyToSend/To{name}Letter.txt', mode = 'w') as letter_to_send:
                letter_to_send.write(new_letter)