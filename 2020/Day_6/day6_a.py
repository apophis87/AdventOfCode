# Evaluating answers
answers = ''
sum = 0
with open('answers.txt') as file:
    for line in file.readlines():
        if line != '\n':
            # Put all the answers of a group in a contiguous string
            answers = answers + line.split('\n')[0]
        else:
            # Converting the string to a set, evaluating number of elements
            # in the set and summing it in each loop to previous intermediate sum
            sum = sum + len(set(answers))
            answers = ''
print(sum)