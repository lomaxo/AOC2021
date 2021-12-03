# with open("test.txt", "w") as file:
#     file.write("testing")

numbers = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
def get_data():
    numbers = []
    with open("AOC2021/input_1_1.txt", 'r') as file:
        for line in file:
            numbers.append(int(line))
    return numbers

def task1():
    last_n = 0
    inc = -1
    for n in get_data():
        if n > last_n:
            inc += 1                
    last_n = n
    print(inc)

def task2():
    last_n = 0
    window = []
    inc = -1
    for n in get_data():
        window.append(n)
        if len(window) > 3:
            window.pop(0)
        print(window, sum(window))
        if len(window) == 3 and sum(window) > last_n:
            inc +=1
        last_n = sum(window)
    print(inc)

# small test change
task2()