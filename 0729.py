import time
import numpy as np

# 미니1
def min_of(lists):
    minimum = lists[0]
    for i in range(1, len(lists)):
        if lists[i] < minimum:
            minimum = lists[i]
    return minimum

# print(min_of(['DTS', 'AAC', 'FLAC']))

# 미니2
def descend_list(lists):
    length = len(lists)
    for i in range(int(length/2)):
        lists[i], lists[length-i-1] = lists[length-i-1], lists[i]      
    return lists
    
"""
x = []
num_length = int(input('원소수 입력 : '))
for i in range(num_length):
    x.append(int(input('x[' + str(i) + ']값 입력 : ')))
print(descend_list(x))
"""

# 미니3
def sequential_search(lists, key): 
    for [index, i] in enumerate(lists):
        if i == key:
            print("IF는 "+str(index+1)+"번 사용.") 
            return index
    print("IF는 "+str(len(lists))+"번 사용.")
    return -1

def sentinel_search(lists, key): # 근데 while말고 for쓰면 보초법 의미있나?
    lists.append(key)
    for [index, i] in enumerate(lists):
        if i == key:
            if index == len(lists)-1:
                print("IF는 "+str(len(lists)+1)+"번 사용.")
                del lists[-1]
                return -1
            else:
                print("IF는 "+str(index+2)+"번 사용.") 
                del lists[-1]
                return index

"""
search_array = [2, 4, 3, 5, 6, 1, 7, 20, 14, 16]
search_number = 14

start_time = time.time()
print(sequential_search(search_array, search_number)) # for 문으로 구현시 빠름
print("time :", time.time() - start_time)
start_time = time.time()
print(sentinel_search(search_array, search_number))
print("time :", time.time() - start_time)
"""

def binary_search(lists, key):
    pl = 0
    pr = len(lists) - 1
    
    while(1):
        pc = (pl + pr) // 2
        if lists[pc] == key:
            return pc
        elif lists[pc] < key:
            pl = pc + 1
        else: pr = pc - 1
        
        if pl > pr : break
    return -1

# search_array = [5, 7, 15 ,28, 29, 31, 39, 58, 68, 70, 95]
# print(binary_search(search_array, 39))

# 실습1
def print_decimal(number):
    decimal = [2]
    for i in range(3, number-1):
        is_it_decimal = True
        for j in decimal:
            if i % j == 0:
                is_it_decimal = False
        if is_it_decimal == 1:
            decimal.append(i)
    return decimal

# print(print_decimal(1000))

# 실습2
def unsort(lists):
    unsort_list_copy = lists.copy()
    unsort_list = []
    for i in range(len(lists)):
        max = np.max(unsort_list_copy)
        unsort_list.append(max)
        unsort_list_copy.remove(max)
    return unsort_list

"""unsort_list = []
while(1):
    msg = input("숫자입력 : ")
    if msg == 'end':
        break
    unsort_list.append(int(msg))
print(unsort(unsort_list))"""

# 실습3
def on_search(lists, key):
    for [index, i] in enumerate(lists):
        if key == i:
            return index
    return -1

# print(on_search([2,5,7,3,1,6], 3))

# 실습4
def on_search_minmax(lists):
    min, max = [lists[0], 0], [lists[0], 0]
    for [index, i] in enumerate (lists):
        if min[0] > i: min = [i, index]
        if max[0] < i: max = [i, index]
    return [min[1], max[1]]

print(on_search_minmax([2,4,6,1,3,9]))