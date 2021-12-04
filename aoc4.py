def get_data(filename):
    with open(filename, 'r') as file:
        calls = file.readline().split(',')
        calls = [int(c) for c in calls]
        cards = [] 
        while True:
            blank = file.readline()
            if not blank:
                break
            lines = []
            for i in range(5):
                lines.append([int(i) for i in file.readline().strip().split()])
            cards.append(BingoCard(lines))

    return calls, cards

class BingoCard:
    def __init__(self, data) -> None:
        self.data = data
        self.tracker = [[0,0,0,0,0] for _ in range(5)]

    def mark_number(self, number):
        for y, line in enumerate(self.data):
            for x, item in enumerate(line):
                if item == number:
                    self.tracker[y][x] = 1

    def check_win(self):
        for line in self.tracker:
            if sum(line) == 5:
                return True
        transpose = list(map(list, zip(*self.tracker)))
        for line in transpose:
            if sum(line) == 5:
                return True
        return False

    def get_score(self):
        sum = 0
        for y, line in enumerate(self.data):
            for x, item in enumerate(line):
                if self.tracker[y][x] == 0:
                    sum += item
        return sum
        

    def __str__(self):
        output = ''
        for y, line in enumerate(self.data):
            for x, item in enumerate(line):
                if self.tracker[y][x] == 0:
                    output+=f' {item:2} '
                else:
                    output += f'*{item:2}*'
            output += '\n'
        return output

def testing():
    calls, cards= get_data('input_4_testing.txt') 
    print(calls, cards)
    for card in cards:
        card.mark_number(8)
        card.mark_number(19)
        card.mark_number(7)
        card.mark_number(25)
        card.mark_number(23)
        print(card)
        print(card.check_win())
    
def task1():
    calls, cards= get_data('input_4.txt') 
    for number in calls:
        for card in cards:
            card.mark_number(number)
            if card.check_win():
                return card.get_score() * number

def task2():
    calls, cards= get_data('input_4.txt')
    winners = []
    while calls:
        number = calls.pop(0)
        for card in cards:
            if not card.check_win():
                card.mark_number(number)
            
                if card.check_win():
                    # print('Winner:')
                    # print(card)
                    # print(card.get_score(), number)
                    # print('-----------')
                    winners.append((card, card.get_score() * number))
                
    return winners
       
print(task2()[-1][1])