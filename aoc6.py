import collections

def get_data(filename):
    with open(filename, 'r') as file:
        numbers = file.read().split(',')
        numbers = [int(n) for n in numbers]
    return numbers

def task1():
    fish = get_data('input_6.txt')
    # print(f'Initial state: {fish}')
    for day in range(80):
        fish = [f-1 for f in fish]
        new_fish = [8] * fish.count(-1)
        fish = [6 if f==-1 else f for f in fish]
        fish.extend(new_fish)
    print(f'Day {day+1}, Total fish: {len(fish)}')

def task2(inputfile, days):
    fish = get_data(inputfile)
    fish_dict = collections.Counter(fish)
    fish_dict_temp = {}
    for day in range(days):
        new_fish = fish_dict[0]
        for i in range(8):
            fish_dict_temp[i] = fish_dict.get(i+1, 0)
        fish_dict_temp[8] = new_fish
        fish_dict_temp[6] += new_fish
        fish_dict = fish_dict_temp
    total_fish = sum(fish_dict.values())
    print(f'Day {day}, Total fish: {total_fish}')
    return total_fish

task1()
task2('input_6.txt', 256)