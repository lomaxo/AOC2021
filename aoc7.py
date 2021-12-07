def get_data(filename):
    with open(filename, 'r') as file:
        data = file.read().strip().split(',')
        data = [int(n) for n in data]
    return data

# print(get_data('input_7_testing.txt'))

def task1(filename):
    data = get_data(filename)
    # average = round(sum(data)/len(data))
    min_fuel = None
    for target in range (0, max(data)):
        movement = [n - target for n in data]
        # print(target, movement)
        abs_movement = [abs(n) for n in movement]
        fuel = sum(abs_movement)
        if not min_fuel or fuel < min_fuel:
            min_fuel = fuel
    return min_fuel


def task2(filename):
    data = get_data(filename)
    # average = round(sum(data)/len(data))
    min_fuel = None
    for target in range (0, max(data)):
        movement = [n - target for n in data]
        # print(target, movement)
        abs_movement = [abs(n) for n in movement]
        fuel = sum([(n**2 + n)/2 for n in abs_movement])
        if not min_fuel or fuel < min_fuel:
            min_fuel = fuel
    return min_fuel


print(f'Task 1: Fuel uses = {task1("input_7.txt")}')

print(f'Task 2: Fuel uses = {task2("input_7.txt")}')