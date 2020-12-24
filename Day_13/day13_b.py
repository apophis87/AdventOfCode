with open('notes.txt', 'r') as file:
    notes = file.readlines()

# second line: lists the bus IDs that are in service according to the shuttle company
# "x" means out of service and can be ignored
services = notes[1].split('\n')[0]
# print(services)

# Extract from the service schedule the IDs of busses running
servicesList = services.split(',')
# print(servicesList)
runningBusses = [int(i) for i in servicesList if i != 'x']
# print(runningBusses) # [17, 41, 523, 13, 19, 23, 787, 37, 29]
offsets = [servicesList.index(str(i)) for i in runningBusses]
# print(offsets)
# save offsets to busses in the list
offsetsDict = {}
for i, bus in enumerate(runningBusses):
    offsetsDict[bus] = offsets[i]
print(offsetsDict)
# apply algorithm explained in https://www.youtube.com/watch?v=4_5mluiXF5I
time = 0
stepSize = runningBusses[0]
for i in range(len(runningBusses)-1):

    while True:
        nextDeparture = time + offsetsDict[runningBusses[i+1]]
        if nextDeparture % runningBusses[i+1] == 0:
            stepSize = stepSize * runningBusses[i+1]
            break
        time = time + stepSize
print(time)
