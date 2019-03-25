######################
# remapping of connectivity graph #
######################
"""
this code remaps the logical mapping by finding shortest path between two qbits and then
moving both qbits

"""


import re
import ast

qbits = [[0,1,2,3,4], [0,0,0,0,0]]

# mapping of hardware topology
g = {0:[1],
1:[0,2],
2:[1,3],
3:[2,4],
4:[3]
}

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

def two_way_swap(g2, length, swaps):
    a = 0
    b = length
    i = swaps/2
    while(i>0):
        g2 = shift_dict_substrings(str(path[a]), str(path[a+1]), "~")
        g2 = shift_dict_substrings(str(path[b]), str(path[b-1]), "~")
        a+=1
        b-=1
        i-=1
    return g2

def make_valid(path):
    g2 = g
    length = len(path)
    swaps = length - 2
    i = 0
    # while not check_valid_op:
    if swaps > 1:
        if swaps%2 == 0:
            two_way_swap(g2 ,length, swaps)
        # improvements requried using two_way_swap()
        """
        relationship b/w length, swaps and iterations is
        for even number of swaps: 
            i = n
            s = n*2
            l = (n*2) + 2
        for odd number of swaps (for imroved version):
            i = n
            s = (n*2) - 1
            l = (n*2) + 1
            (for current version):
            i = s

            need of mathematical improvements
        """
    while i < swaps:
        g2 = shift_dict_substrings(str(path[i]), str(path[i+1]), "~")
        i+=1
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
    # checks if 2-qbit op
    if(len(subList) == 2):
        # checks if valid op based on topology
        if check_valid_op(int(subList[0]), int(subList[1])):
            pass
        # if not valid then makes it valid by moving 2nd qbit
        else:
            path = find_shortest_path(g, int(subList[0]), int(subList[1]))
            g = make_valid(path)
fo.close()
# print("------------------------------------------")
# print("Qubit\t\tdouble bit")
# print("------------------------------------------")
# print(path)
# for i in range(0, 5):
#      2==2
#     print(str(i) + "\t\t" + str(doubleBit[i]))
