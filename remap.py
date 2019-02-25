######################
# remapping of connectivity graph #
######################
import re
import ast

qbits = [[0,1,2,3,4], [0,0,0,0,0]]

g = {0:[1],
1:[0,2],
2:[1,3],
3:[2,4],
4:[3]
}
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

def shift_dict_substrings(s1, s2, temp):
    ret_str = str(g).replace(s1, temp).replace(s2, s1).replace(temp, s2)
    return dict(ast.literal_eval(ret_str))

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

def make_valid(path):
    length = len(path) - 2
    i = 0
    # while not check_valid_op:
    while i < length:
        g2 = shift_dict_substrings(str(path[i]), str(path[i+1]), "~")
        i+=1
    # g = g2 is is here, are python dicts immutable? ans: no, some other problem
    return(g2)


#############################################
# Function defination end
############################################
fo = open('code1.txt')
while True:
    str1 = fo.readline()
    if(str1==''):
        break
    ## regex for extracting digits from a string, returns as char
    subList = re.findall('\d', str1)
    if(len(subList) == 2):
        if check_valid_op(int(subList[0]), int(subList[1])):
            # print('valid')
            2==2
        else:
            # print('invalid')
            print('before update')
            print(g)
            path = find_shortest_path(g, int(subList[0]), int(subList[1]))
            # g = make_valid(g, path) ### issue here check find_shortest_path()
            g = make_valid(path)
            print('after update')
            print(g)
            if check_valid_op(int(subList[0]), int(subList[1])):
                # 2==2
                print('valid')
    else:
        2==2
fo.close()
print("------------------------------------------")
print("Qubit\t\tdouble bit")
print("------------------------------------------")
print(path)
for i in range(0, 5):
     2==2
#     print(str(i) + "\t\t" + str(doubleBit[i]))
