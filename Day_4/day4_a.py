# Evaluate credentials
valid = 0
count = 0
# List for collecting fields of persons
content = []
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
                valid = valid + 1
            # Make an exception for credentials missing only cid
            if len(content) == 7:
                cid = False
                for item in content:
                    if item.split(':')[0] == 'cid':
                        cid = True
                if not cid:
                    valid = valid + 1
            # Reset the list for the next credentials
            content = []

print("\"Valid\" credentials: ", valid)