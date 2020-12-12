# Get the instructions in the bootcode into a list
bootcode = []
with open('bootcode.txt') as file:
    for line in file.readlines():
        bootcode = bootcode + [''.join(line.split('\n')[:-1])]

#print(bootcode)

accumulator = 0

def interpreter(ip, instruction):
    global accumulator
    operation = instruction.split()[0]
    if operation == 'acc':
        argument = instruction.split()[1]
        # Distinguish if operation is addition or subtraction and
        # perform operation on accumulator
        if argument[0] == '+':
            accumulator = accumulator + int(argument.split('+')[1])
        if argument[0] == '-':
            accumulator = accumulator - int(argument.split('-')[1])
        return ip + 1
    elif operation == 'nop':
        # No operation returns incremented instruction pointer
        return ip + 1
    elif operation == 'jmp':
        offset = instruction.split()[1]
        if offset[0] == '+':
            return ip + int(offset.split('+')[1])
        if offset[0] == '-':
            return ip - int(offset.split('-')[1])




ip = 0

track_ips = []

while True:
    try:
        if ip in track_ips:
            break
        else:
            track_ips = track_ips + [ip]
        instruction = bootcode[ip]
        ip = interpreter(ip, instruction)

    except:
        break
print('Accumulator = ', accumulator)

