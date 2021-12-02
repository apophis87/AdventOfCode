# Evaluating answers
import string
# All the lowercase letters in a set
answers = set(string.ascii_lowercase)
sum = 0
with open('answers.txt') as file:
    for line in file.readlines():
        if line != '\n':
            # Put all the answers of a group in a contiguous string
            line_set = set(line.split('\n')[0])
            answers = answers.intersection(line_set)
        else:
            # Converting the string to a set, evaluating number of elements
            # in the set and summing it in each loop to previous intermediate sum
            # print(answers)
            # print(100*'-')
            sum = sum + len(answers)
            answers = set(string.ascii_lowercase)
print(sum)