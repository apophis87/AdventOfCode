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

def changeCode(operation):
    if 'jmp' in operation:
        operation.replace('jmp', 'nop')
    elif 'nop' in operation:
        operation.replace('nop', 'jmp')
    return operation

while True:
    try:
        if ip not in track_ips:
            track_ips.append(ip)
            ip = interpreter(ip, bootcode[ip])
        else:
            nip = track_ips[-1]
            ip = interpreter(nip, changeCode(bootcode[nip]))
        print(ip)
    except:
        if ip == len(bootcode):
            print('Finished normally')
        else:
            print('Something went wrong :(')
        break

print(accumulator)