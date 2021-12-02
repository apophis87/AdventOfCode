# Get the instructions in the bootcode into a list
bootcode = []
with open('bootcode.txt') as file:
    for line in file.readlines():
        bootcode = bootcode + [''.join(line.split('\n')[:-1])]

# print(bootcode)

accumulator = 0

# this method interprets the code and performs the operations
# it returns the instruction pointer (index in the list) and
# accumulates to the global variable
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

# this method is only supposed to switch a jmp instruction
# with a nop instruction
def changeCode(instruction):
    instruction = instruction.split()
    if instruction[0] == 'jmp':
        instruction[0] = 'nop'
    elif instruction[0] == 'nop':
        instruction[0] = 'jmp'
    return ' '.join(instruction)

# this method performs the code entirely without any change to the bootcode
def programm(bootcode):
    global accumulator
    ip = 0
    track_ips = []
    limit = 0
    success = False
    accumulator = 0
    while limit < 1000:
        try:
            if ip in track_ips:
                accumulator = 0
                break
            track_ips.append(ip)
            ip = interpreter(ip, bootcode[ip])
        except:
            if ip == len(bootcode):
                print('End of programm, accumulator is: ', accumulator)
                success = True
                break
        limit = limit + 1
    return success

# For every nop and jmp in the bootcode the programm is run
# by changing successively each nop or jmp. If the program runs
# until the end of the bootcode, it will break the loop.
# BRUTEFORCE... :(
for index, line in enumerate(bootcode):
    if line.split()[0] == 'jmp' or line.split()[0] == 'nop':
        print(100*'-')
        print('Change instruction ', bootcode[index])
        bootcode[index] = changeCode(bootcode[index])
        print('Now running with instruction ', bootcode[index])
        accumulator = 0
        if programm(bootcode):
            print('Success!')
            break
        else:
            bootcode[index] = changeCode(bootcode[index])
            print('Failed!')
            print('Change back instruction to ', bootcode[index])
