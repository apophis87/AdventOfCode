with open("input.txt") as file:
    input_data = file.read().split(',')
    input_data = [int(i) for i in input_data]

max_pos = max(input_data)
min_pos = min(input_data)

print(min_pos, max_pos)

fuel_costs_list = [] # total fuel costs to move to position corresponding to index in list
for pos in range(min_pos, max_pos):
    fuel_cost = 0
    for current_pos in input_data:
        fuel_cost += abs(current_pos-pos)
    fuel_costs_list.append(fuel_cost)

least_cost = min(fuel_costs_list)
pos_least_cost = fuel_costs_list.index(least_cost)

print(f"Least fuel costs are {least_cost} when all crabs move to position {pos_least_cost}")