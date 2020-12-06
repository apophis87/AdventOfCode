import re

# Evaluate credentials
valid = 0
count = 0
# List for collecting fields of persons
content = []

# This method checks the fields according to the rules  and returns
# 'int' 0 if invalid or 'int' 1 if valid
def validate(content):
    pattern_hcl = re.compile('^#([0-9a-f]{6})$')
    pattern_pid = re.compile('^[0-9]{9}$')

    validity = 1
    for item in content:
        key = item.split(':')[0]
        value = item.split(':')[1]
        if key == 'byr':
            if int(value) < 1920 or int(value) > 2002:
                validity = 0
                break
        elif key == 'iyr':
            if int(value) < 2010 or int(value) > 2020:
                validity = 0
                break
        elif key == 'eyr':
            if int(value) < 2020 or int(value) > 2030:
                validity = 0
                break
        elif key == 'hgt':
            if 'cm' in value:
                hgtcm = int(value.split('cm')[0])
                if hgtcm < 150 or hgtcm > 193:
                    validity = 0
                    break
            elif 'in' in value:
                hgtin = int(value.split('in')[0])
                if hgtin < 59 or hgtin > 76:
                    validity = 0
                    break
            else:
                validity = 0
                break
        elif key == 'hcl':
            if not pattern_hcl.match(value):
                validity = 0
        elif key == 'ecl':
            if value not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                validity = 0
        elif key == 'pid':
            if not pattern_pid.match(value):
                validity = 0
                break
    return validity


with open('credentials.txt') as file:
    for line in file.readlines():
        # Split the items on the line
        items = line.split()
        # Check if line is empty
        if items:
            # Gather fields in a list
            content = content + items
        else:
            # Evaluate list
            if len(content) == 8:
                # if valid, validate returns 1 and the count 'valid' increments by 1
                valid = valid + validate(content)
            # Make an exception for credentials missing only cid
            if len(content) == 7:
                cid = False
                for item in content:
                    if item.split(':')[0] == 'cid':
                        cid = True
                if not cid:
                    # if valid, validate returns 1 and the count 'valid' increments by 1
                    valid = valid + validate(content)
            # Reset the list for the next credentials
            content = []

print("\"Valid\" credentials: ", valid)