def get_data(filename):
    grid = []
    with open(filename, 'r') as file:
        for line in file:
            row = []
            for digit in line.strip():
                row.append(int(digit))
            grid.append(row)
    return grid

# print(get_data('input_9_testing.txt'))

def is_min(grid, x, y):
    s = 0
    n = grid[y][x]
    if x>0 and n >= grid[y][x-1]:
        return False
    if x < len(grid[y])-1 and n >= grid[y][x+1]:
        return False
    if y > 0 and n >= grid[y-1][x]:
        return False
    if y < len(grid)-1 and n >= grid[y+1][x]:
        return False
    return True

def get_low_points(grid):
    height = len(grid)
    width = len(grid[0])
    low_points = []
    for y in range(height):
        for x in range(width):
            if is_min(grid, x ,y):
                low_points.append((x,y))
    return low_points

def task1(filename):
    grid = get_data(filename)
    height = len(grid)
    width = len(grid[0])
    low_points = []
    for y in range(height):
        for x in range(width):
            if is_min(grid, x ,y):
                low_points.append((x,y))
    
    print(low_points)
    s = 0
    for point in low_points:
        x, y = point
        print(grid[y][x])
        s += grid[y][x] + 1
    return s

def get_neighbours(point, grid):
    s = 0
    x, y = point
    n = grid[y][x]
    ret_points = []
    if x>0 and grid[y][x-1] < 9:
        ret_points.append((x-1,y))
    if x < len(grid[y])-1 and grid[y][x+1] < 9:
        ret_points.append((x+1,y))
    if y > 0 and grid[y-1][x] < 9:
        ret_points.append((x,y-1))
    if y < len(grid)-1 and grid[y+1][x] < 9:
        ret_points.append((x,y+1))
    return ret_points



# print(task1('input_9.txt'))
def task2(filename):
    grid = get_data(filename)
    low_points = get_low_points(grid)
    print(low_points)
    sizes = []
    for low in low_points:
        point_queue = [low]
        size = 0
        while len(point_queue) > 0:
            p = point_queue.pop()
            neighbours = get_neighbours(p, grid)
            for n in neighbours:
                size += 1
                x, y = n
                grid[y][x] = 9
            point_queue.extend(neighbours)
        print(low, size)
        sizes.append(size)
    sizes.sort()
    print(sizes)
    print(sizes[-3]* sizes[-2] * sizes[-1])

task2('input_9.txt')