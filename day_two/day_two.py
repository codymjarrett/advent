
def readFile():
    contents = []
    with open("input.txt") as f:
        for line in f.readlines():
            contents.append(line)
        f.close()
    return contents


def format_data():
    data = readFile()
    return data

def get_occurances(letters, target):
    count = 0
    for i, v in enumerate(letters): 
        if v == target:
            count = count + 1
    return count  


def get_dictionary(i):
    my_dict = {}
    index = 0
    for x in i:
        index = index + 1
        colon_index = x.rfind(':')
        key = x[0:colon_index - 2]
        value = x[colon_index + 1:]
        target = x[colon_index - 1]
        my_dict[key + '-' + str(index)] = {
            'value': value.lstrip().strip('\n'),
            'target': target,
            'range': key
        }
    return my_dict

def solve():
    i = format_data()
    my_dict = get_dictionary(i)
    print(my_dict)
    count = 0

    for x in my_dict:
        minimun = my_dict[x]['range'].split('-')[0]
        maximum = my_dict[x]['range'].split('-')[1]
        value = my_dict[x]['value']
        target = my_dict[x]['target']
        occurances = get_occurances(value, target)
        if occurances in range(int(minimun), int(maximum) + 1):
            count += 1
    return count


print(solve()) 
