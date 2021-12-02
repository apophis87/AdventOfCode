# Recursion for finding number of bags that are contained in a 'shiny gold' bag
import re

# This lambda function removes text and punctuation. Result is a list like [dark green,5 vibrant green,4 clear blue]
# instead of "dark green bags contain 5 vibrant green bags, 4 clear blue bags."
repl = lambda t: line.replace(' bags contain ', ',').replace(' bags', '').replace('.', '').replace(' ,', ','). \
    replace('\n', '').replace(' bag', '').replace(', ', ',').split(',')

# Read rules.txt and make a list containing the rules as lists
rules = []
with open('rules.txt') as file:
    for line in file.readlines():
        rule = repl(line)
        rules.append(rule)

# print(rules)
# Recursive method
def checkRule(listofrules, bag):
    # Find the rule
    for rule in listofrules:
        if rule[0] == bag:
            break
    # empty bag contains the string 'no other'
    # since the word 'bag' has already been removed
    if rule[1] == 'no other':
        return 0
    else:
        # Collect the terms in a list and call the method
        # recursively until 'no other' is found in the rule
        terms = []
        for item in rule[1:]:
            num_sub = int(item.split()[0])
            bag_sub = ' '.join(item.split()[1:])
            print(num_sub, bag_sub)
            terms = terms + [num_sub*(1 + checkRule(rules, bag_sub))]
        return sum(terms)


input = r'shiny gold'
print('return', checkRule(rules, input))


