# Bus ID number indicates how often the bus leaves for the airport
# Bus schedules are defined based on a timestamp that measures the number of minutes
# since some fixed reference point

with open('notes.txt', 'r') as file:
    notes = file.readlines()

# first line: estimate of earliest timestamp you could depart on a bus
estimate = int(notes[0].split('\n')[0])
# print(estimate)

# second line: lists the bus IDs that are in service according to the shuttle company
# "x" means out of service and can be ignored
services = notes[1].split('\n')[0]
# print(services)

# Extract from the service schedule the IDs of busses running
servicesList = services.split(',')
# print(servicesList)
runningBusses = [int(i) for i in servicesList if i != 'x']
# print(runningBusses) # [17, 41, 523, 13, 19, 23, 787, 37, 29]

# Figure out the earliest bus you can take to the airport (exactly one)

waitingTimes = [(estimate//id + 1)*id-estimate for id in runningBusses]
# print(waitingTimes)

# Result: ID of the earliest bus I can take multiplied by number of minutes I have to wait
min_wait = min(waitingTimes)
index = waitingTimes.index(min_wait)
min_id = runningBusses[index]
print('Result is: ', min_id*min_wait)
