data = ['00100','11110','10110','10111','10101',
'01111',
'00111',
'11100',
'10000',
'11001',
'00010',
'01010']

def get_data():
    numbers = []
    with open("input_3_1.txt", 'r') as file:
        for line in file:
            numbers.append(line)
    return numbers

def task1():
    data = get_data()
    length = len(data)    
    print(data)
    gamma = ''
    epsilon = ''
    for bit_i in range(12):
        bit_sum = 0
        for datum in data:
            bit_sum += int(datum[bit_i])
        gamma += '1' if bit_sum > length/2 else '0'
        epsilon += '0' if bit_sum > length/2 else '1'
    print(gamma, epsilon, int(gamma, 2) * int(epsilon, 2))

# task1()
def most_common_bit_value(data, bit_i, default='1'):
    length = len(data)    
    bit_sum = 0
    for datum in data:
        bit_sum += int(datum[bit_i])
    if bit_sum == length/2:
        return default
    else:
        return '1' if bit_sum > length/2 else '0'

def least_common_bit_value(data, bit_i, default='0'):
    length = len(data)    
    bit_sum = 0
    for datum in data:
        bit_sum += int(datum[bit_i])
    if bit_sum == length/2:
        return default
    else:
        return '0' if bit_sum > length/2 else '1'

def filter_data(data, bit_i, value):
    ret_data = []
    for datum in data:
        if datum[bit_i] == str(value):
            ret_data.append(datum)
    return ret_data

def task2():
    data = get_data() #['00100','11110','10110','10111','10101','01111','00111','11100','10000','11001','00010','01010']
    print(most_common_bit_value(data, 1))
    print(data)
    data = filter_data(data, 0, 0)
    print(data)
    # Oxygen
    data = get_data() #['00100','11110','10110','10111','10101','01111','00111','11100','10000','11001','00010','01010']
    for bit_i in range(12):
        data = filter_data(data, bit_i, most_common_bit_value(data, bit_i))
        if len(data) == 1:
            oxygen = int(data[0],2)
            break
    
    # CO2
    data = get_data() #['00100','11110','10110','10111','10101','01111','00111','11100','10000','11001','00010','01010']
    for bit_i in range(12):
        data = filter_data(data, bit_i, least_common_bit_value(data, bit_i))
        if len(data) == 1:
            co2 = int(data[0],2)
            break
    
    return oxygen, co2, oxygen*co2

print(task2())
    

