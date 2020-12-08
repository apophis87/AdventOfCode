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

# This method returns a list of bags for which the given bag can be contained
# When giving a list with the skip input, items in the list will be skipped
def checkRule(listofrules, pattern, skip=[]):
    listofbags = []
    for rule in listofrules:
        # rule[0] is the name of the bag for that rule
        if rule[0] not in skip:
            # Check the remaining items in the list for the pattern
            for item in range(1, len(rule)):
                if re.search(pattern, rule[item]):
                    # Add the item to the list of bags for which the pattern
                    # is contained
                    listofbags = listofbags + [rule[0]]
    return listofbags

# Initial search with the starting pattern = the original bag
original_bag = r'shiny gold'
pattern = original_bag
skip = []
bags_tot = checkRule(rules, pattern, skip=skip)
# Flag for breaking the while loop
stop = False

# The bags_tot list should be empty at the end
# The skip list should be full with all possible bags for which it is possible they contain
# eventually at least one original bag (shiny gold)
while bags_tot and not stop:
    for i in bags_tot:
        bags_tot = bags_tot + checkRule(rules, pattern=i, skip=skip)
        # print('For ', bags_tot)
        try:
            s = set(bags_tot)
            s.remove(i)
            bags_tot = list(s)
        except:
            print('Element not removable.')
            stop = True
        # Add the element checked to the skip list
        skip = skip + [i]

print(f'Number of bags that can contain a \"{original_bag}\" bag: ', len(skip))