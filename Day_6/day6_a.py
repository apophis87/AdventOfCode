# Evaluating answers
answers = ''
with open('answers.txt') as file:
    for line in file.readlines():
        if line:
            # Gather fields in a list
            answers = answers + line
        else:
            print(answers)
            answers = ''
