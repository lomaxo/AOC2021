def get_data(filename):
    with open(filename, 'r') as file:
        data = []
        for line in file:
            data.append(line.strip())
    return data

def get_incomplete(data):
    pairs = {'[': ']', '{':'}','(':')','<':'>'}
    points = {')': 3, ']': 57, '}': 1197, '>': 25137}
    ret_data = []
    for line in data:
        stack = []
        for c in line:
            if c in '[({<':
                stack.append(c)
            elif c in '])}>':
                popped = stack.pop()
                if pairs[popped] != c:
                    break
        else:
            ret_data.append(line)
    return ret_data

    
def task1(filename):
    data = get_data(filename)
    pairs = {'[': ']', '{':'}','(':')','<':'>'}
    points = {')': 3, ']': 57, '}': 1197, '>': 25137}
    score = 0
    for line in data:
        stack = []
        for c in line:
            if c in '[({<':
                stack.append(c)
            elif c in '])}>':
                popped = stack.pop()
                if pairs[popped] != c:
                    print(f'Error: expected {pairs[popped]}, found {c}')
                    score += points[c]
    return score

def task2(filename): 
    data = get_data(filename)
    data = get_incomplete(data)
    scores = []
    for line in data:
        stack = []
        for c in line:
            if c in '[({<':
                stack.append(c)
            elif c in '])}>':
                stack.pop()
        stack.reverse()
        print(stack)
        points = {'(': 1, '[': 2, '{': 3, '<': 4}
        line_score = 0
        for bracket in stack:
            line_score *= 5
            line_score += points[bracket]
        scores.append(line_score)
    scores.sort()
    return scores[len(scores)//2]
            
print(task2('input_10.txt'))