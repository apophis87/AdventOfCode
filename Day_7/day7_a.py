import re
repl = lambda t: line.replace(' bags contain ', ',').replace(' bags', '').replace('.', '').replace(' ,', ',').replace('\n','').replace(' bag','').split(',')
pattern = 'shiny gold'
bags =[]
bags_tot = []
with open('rules.txt') as file:
    for line in file.readlines():
        rule = repl(line)
        for i in range(1,len(rule)):
            if re.search(pattern,rule[i]):
                bags = bags + [rule[0]]
    for bag in bags:
        pattern = bag
        for line in file.readlines():
            rule = repl(line)
            print('o')
            for i in range(1, len(rule)):
                if re.search(pattern, rule[i]):
                    print(rule[0])
                    bags_tot = bags_tot + [rule[0]]

    print(bags_tot)