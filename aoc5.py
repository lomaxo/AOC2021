
def get_data(filename):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(' -> ')
            start = [int(n) for n in parts[0].split(',')]
            end = [int(n) for n in parts[1].split(',')]
            data.append((start, end))
        return data

def task1():
    data = get_data('input_5.txt')
    grid = [[0]*1000 for _ in range(1000)]
    for line in data:
        start, end = line
        # vertical
        if start[0] == end[0]:
            dir = 1 if  start[1] < end[1] else -1
            for y in range(start[1], end[1] + dir, dir):
                grid[y][start[0]] += 1
        # horizontal
        elif start[1] == end[1]:
            dir = 1 if  start[0] < end[0] else -1
            for x in range(start[0], end[0] + dir, dir):
                grid[start[1]][x] += 1
        # diagonal
        else:
            xdir = 1 if start[0] < end[0] else -1
            ydir = 1 if start[1] < end[1] else -1
            x = start[0]
            y = start[1]
            while x != end[0] + xdir:
                grid[y][x] += 1
                x += xdir
                y += ydir
        
    # print(grid)
    # count overlaps
    count = 0
    for row in grid:
        for x in row:
            if x > 1:
                count += 1
    return count
            
print(task1())