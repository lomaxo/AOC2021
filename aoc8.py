import itertools

def get_data(filename):
    data_lines = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.split('|')
            digits = parts[0].strip().split(' ')
            code = parts[1].strip().split(' ')
            data_lines.append((digits,code))
    return data_lines

def task1(filename):
    data = get_data(filename)
    cipher = [0]*10
    for line in data:
        digits = line[1]
        print(digits)
        for digit in digits:
            if len(digit) == 2:
                cipher[1] += 1
            elif len(digit) == 4:
                cipher[4] += 1
            elif len(digit) == 3:
                cipher[7] += 1
            elif len(digit) == 7:
                cipher[8] += 1
        print(cipher)
    print(sum(cipher))

# A lot of messing about trying to find a clever solution....
def task2_old(filename):
    data = get_data(filename)
    cipher = [0]*10
    all_segments = set(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
    possible_mapping = {'a': all_segments.copy(), 'b': all_segments.copy(),'c': all_segments.copy(),'d': all_segments.copy(),
                'e': all_segments.copy(),'f': all_segments.copy(),'g': all_segments.copy()}
    correct_map = [set(['A','B','C','E','F','G']), set(['C','F']), set(list('ACDEG')), set(list('ACDFG')), set(list('BCDF')), set(list('ABDFG')), set(list('ABDEFG')), set(list('ACF')), set(list('ABCDEFG')), set(list('ABCDFG'))]
    print(correct_map)
    print(possible_mapping)
    # for line in data:
    digits = data[0][0]
    print(digits)
    for i in [1,4,7,8,2,3,5,0,6,9]:
        print(f'Finding possible {i}')
        candidates = list(filter(lambda x: len(x) == len(correct_map[i]), digits))
        candidates = [''.join(sorted(c)) for c in candidates]
        print(f'candidates: {candidates}')
        print(f'Output: {correct_map[i]}')
        for candidate in candidates:
            for segment in candidate:
                possible_mapping[segment] = possible_mapping[segment].intersection(correct_map[i])
                print(f'segment {segment} -> {correct_map[i]}, possible={possible_mapping[segment]} ')

def is_map_valid(map, code):
    displays = [[0,1,2,4,5,6],[2,5], [0,2,3,4,6], [0,2,3,5,6], [1,2,3,5],[0,1,3,5,6],[0,1,3,4,5,6],[0,2,5],[0,1,2,3,4,5,6],[0,1,2,3,5,6]]
    code = [''.join(sorted(c)) for c in code]
    # print(code)
    for digit in range(10):
        output = ''
        for s in displays[digit]:
            output += map[s]

        if ''.join(sorted(output)) not in code:
            return False

    return True            

def find_map(numbers):
    posible_map = list(itertools.permutations('abcdefg', 7))
    posible_map = [''.join(s) for s in posible_map]
    for map in posible_map:
        if is_map_valid(map, numbers):
            return map
    print('No map found!')
    return False
    
def decode(map, input):
    displays = [[0,1,2,4,5,6],[2,5], [0,2,3,4,6], [0,2,3,5,6], [1,2,3,5],[0,1,3,5,6],[0,1,3,4,5,6],[0,2,5],[0,1,2,3,4,5,6],[0,1,2,3,5,6]]
    disp_dict = {}
    input = ''.join(sorted(input))
    for digit in range(10):
        output = ''
        for s in displays[digit]:
            output += map[s]
        disp_dict[''.join(sorted(output))] = digit
    return disp_dict[input]

def task2(filename):
    data = get_data(filename)
    sum = 0
    for line in data:
        numbers = line[0]
        code = line[1]
        map = find_map(numbers)
        # print(map, end=' ')
        output = ''
        for d in code:
            output += str(decode(map, d))
        # print(output)
        sum += int(output)
    return sum
          
print(task2('input_8.txt'))
