
def readFile():
    contents = []
    with open("input.txt") as f:
        for line in f.readlines():
            contents.append(int(line))
        f.close()
    return contents



def solve():
    input = readFile()
    my_set = set()
    for x in input:
        difference = 2020 - x
        if difference in my_set:
            return x * difference
        my_set.add(x)

     

print(solve())