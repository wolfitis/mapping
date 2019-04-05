
import re
import ast

qbits = [[0,1,2,3,4], [0,0,0,0,0]]

# reading of topology
fo = open('topology.txt')
str2 = fo.readline()
g = dict(ast.literal_eval(str2))

# mapping of hardware topology
# g = {0:[1],
# 1:[0,2],
# 2:[1,3],
# 3:[2,4],
# 4:[3]
# }

# hardware topology 
topology = g

#############################################
# Function defination begins
############################################
def check_valid_op(bit1, bit2):
    """
    Takes two bits and checks if second bit is found against first bit in dictionary.
    bit1 -> int
    bit2 -> int

    Returns:
    true/false based on the result
    """
    if bit1 in g:
        if bit2 in g[bit1]:
            return True
    return False

# def shift_dict_substrings(s1, s2, temp):
#     ret_str = str(g).replace(s1, temp).replace(s2, s1).replace(temp, s2)
#     return dict(ast.literal_eval(ret_str))

def find_shortest_path(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not start in g:
            return None
        shortest = None
        for node in graph[start]:
            if node not in path:
                newpath = find_shortest_path(graph, node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest

# def make_valid(path):
#     g2 = g
#     length = len(path) - 2
#     i = 0
#     # while not check_valid_op:
#     while i < length:
#         g2 = shift_dict_substrings(str(path[i]), str(path[i+1]), "~")
#         i+=1
#     return(g2)


# Function defination end ################################
swaps = [] # to count the swaps of individual instructions
timetaken = [] # to count the time of individual instructions
swap_count = 0
total_time = 0
fo = open('code1.txt')
while True:
    str1 = fo.readline()
    if(str1==''):
        break
    subList = re.findall('\d', str1)
    if(len(subList) == 2):
        if check_valid_op(int(subList[0]), int(subList[1])):
            timetaken.append(2)
            total_time+=2
            pass
        else:
            path = find_shortest_path(g, int(subList[0]), int(subList[1]))
            # g = make_valid(path)
            # swaps will be equal to paths length 0000000000000000 ?
            swap_count = len(path)
            swaps.append(swap_count)
            timetaken.append(2 + (swap_count * 6))
            total_time+=2 + (swap_count * 6)
            # 6 becoz 3 cnot for 1 swap, 1 cnot takes 2ms so 1 swap is = (3*2) = 6ms
    else:
        swaps.append(0)
        timetaken.append(1)
        total_time+=1
fo.close()
print(swaps)
print(swap_count)
print(timetaken)
print(total_time)