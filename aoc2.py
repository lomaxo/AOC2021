data = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""
data = data.split('\n')

def task1():
    with open('input_2_1.txt', 'r') as data:
        depth = 0
        distance = 0

        for line in data:
            instruction, value = line.split()
            value = int(value)
            print(instruction, value)
            if instruction == 'forward':
                distance += value
            elif instruction == 'up':
                depth -= value
            elif instruction == 'down':
                depth += value
            else:
                print("ERROR: Unexpected instruction")

        print(f'depth: {depth}, distance: {distance}')
        print(f'distance x depth: {distance * depth}')

# task1()
def task2():
    with open('input_2_1.txt', 'r') as data:
        depth = 0
        distance = 0
        aim = 0
        for line in data:
            instruction, value = line.split()
            value = int(value)
            print(instruction, value)
            if instruction == 'forward':
                distance += value
                depth += aim * value
            elif instruction == 'up':
                aim -= value
            elif instruction == 'down':
                aim += value
            else:
                print("ERROR: Unexpected instruction")

        print(f'depth: {depth}, distance: {distance}')
        print(f'distance x depth: {distance * depth}')

task2()