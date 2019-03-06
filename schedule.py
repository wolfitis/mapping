# for now this code is working 
# teeling us about ignorable gates
import re

#############################################
# Function defination begin
#############################################

# function to check ignorable gates
def ignorable(my_code):
    my_code2 = []
    q1 = ""
    q2 = ""
    cancell_i1 = -1
    cancell_i2 = -1
    consecutive = False
    for i in range(len(my_code)):
        ## regex for extracting digits from a string, returns as char
        str1 = my_code[i]
        subList = re.findall('\d', str1)
        my_code2.append(str1)
        if(len(subList) == 2 and consecutive is False):
            q1 = subList[0]
            q2 = subList[1]
            consecutive = True
            cancell_i1 = len(my_code2) - 1
            continue
        if(len(subList)==2 and ((q1 == subList[0] and q2 == subList[1]) and consecutive)):
            # print("cancell")
            cancell_i2 = len(my_code2) - 1
            # print(len(my_code))
            # print('i1 ',cancell_i1)
            # print('i2 ',cancell_i2)
            # print('val', my_code[cancell_i2])
            my_code[cancell_i1] = '4'
            my_code[cancell_i2] = '4'
            # print(q1)
            # print(q2)
            # print(my_code[cancell_i2])
            consecutive = False
            continue
        # print(type(subList[0]))
        # my_code.append = subList
        # my_code = subList
        # my_code.append(subList)
        if(len(subList) == 2):
            cancell_i1 = len(my_code2) - 1
            q1 = subList[0]
            q2 = subList[1]
            # print(q1)
            # print(type(q1))
            # print(q2)
            # print(type(q2))
            # print(subList[0])
            # print(subList[1])
            # print('-----')
            # print(type(subList[0]))
            2==2
        else:
            2==2
    # return my_code2

#############################################
# Function defination end
#############################################




fo = open('code2.txt')
my_code = []
while True:
    str1 = fo.readline()
    if(str1==''):
        break
    
    my_code.append(str1)
fo.close()
print(len(my_code))
ignorable(my_code)
# my_code4 = ignorable(my_code)
fo2 = open('code4.txt', 'w')
for i in range(len(my_code)):
    if my_code[i] == '4':
        continue
    fo2.write(my_code[i])
fo2.close()
# print(my_code)
# print(my_code[0])
# print(my_code[15])