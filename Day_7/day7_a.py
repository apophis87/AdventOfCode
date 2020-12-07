import re
repl = lambda t: line.replace(' bags contain ', ',').replace(' bags', '').replace('.', '').replace(' ,', ',').replace('\n','').replace(' bag','').split(',')
pattern = 'shiny gold'
with open('rules.txt') as file:
    for line in file.readlines():
        rule = repl(line)
        for i in range(1,len(rule)):
            if re.search(pattern,rule[i]):
                print(rule)