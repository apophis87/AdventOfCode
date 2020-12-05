# Read the list of inputs saved in passwords.txt
counter = 0
with open('passwords.txt') as file:
    for pw in file.readlines():
        # Separate password and policy
        policy, password = pw.split(':')
        # Get policy details
        firstPos = int(policy.split()[0].split('-')[0])
        secondPos = int(policy.split()[0].split('-')[1])
        letter = policy.split()[1]
        # Determine if policy holds (XOR)
        if (password[firstPos] == letter) ^ (password[secondPos] == letter):
            counter = counter + 1

print('Passwords matching inteded policy: ', counter)
