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

def checkRule(listofrules, bag):
    for rule in listofrules:
        if rule[0] == bag:
            break

    if rule[1] == 'no other':
        return 2
    else:
        terms = []
        for item in rule[1:]:
            num = int(item.split()[0])
            bag = ' '.join(item.split()[1:])
            terms = terms + [num*checkRule(rules, bag)]
        return sum(terms)


input = r'shiny gold'

print(checkRule(rules, input))


