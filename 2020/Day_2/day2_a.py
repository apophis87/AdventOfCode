# Read the list of inputs saved in passwords.txt
counter = 0
with open('passwords.txt') as file:
    for pw in file.readlines():
        # Separate password and policy
        policy, password = pw.split(':')
        # Get policy details
        minReps = int(policy.split()[0].split('-')[0])
        maxReps = int(policy.split()[0].split('-')[1])
        letter = policy.split()[1]
        # Determine if policy holds
        if int(password.count(letter)) in range(minReps, maxReps+1):
            counter = counter + 1

print('Passwords matching policy: ', counter)

