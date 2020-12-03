# Read the list of inputs saved in passwords.txt
with open('passwords.txt') as file:
    for pw in file.readlines():
        policy, password = pw.split(':')
        print(policy, password)


