with open("input1.txt") as file:
    input_data = [line.split('\n')[0] for line in file.readlines()]

print(input_data)

for line in input_data:
    if not len(line)%2:
        print(line)


print(input_data[0].count('{'))
print(input_data[0].count('}'))
print(input_data[0].count('['))
print(input_data[0].count(']'))
print(input_data[0].count('('))
print(input_data[0].count(')'))
print(input_data[0].count('<'))
print(input_data[0].count('>'))