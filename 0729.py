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

# print(on_search_minmax([2,4,6,1,3,9]))

# q0
def question_0(lists, number):
    return_list = []
    for i in lists:
        if i < number:
            return_list.append(i)
    return return_list

"""
N, X = map(int, input().split())
data = list(map(int, input().split()))
answer = question_0(data, X)
print(answer)
"""

# q1
def question_1(lottos, win_nums):
    joker = 0
    check = 0
    for i in lottos:
        if i == 0:
            joker = joker + 1
        for j in win_nums:
            if i == j:
                check = check + 1
    answer = []
    answer.append(7 - (check + joker))
    if 7 - check == 7:
        answer.append(6)
    else:
        answer.append(7 - check)
    return answer

# lottos = [44, 1, 0, 0, 31, 25]
# win_nums = [31, 10, 45, 1, 6, 19]
# lottos = [0, 0, 0, 0, 0, 0]
# win_nums = [38, 19, 20, 40, 15, 25]
# lottos = [45, 4, 35, 20, 3, 9]
# win_nums = [20, 9, 3, 45, 4, 35]
# answer = question_1(lottos, win_nums)
# print(answer)

# q2
def question_2(numbers):
    answer = 0
    for i in range(10):
        answer = answer + i
        for j in numbers:
            if i == j:
                answer = answer - i
    return answer

# numbers = [1,2,3,4,6,7,8,0]
# print(question_2(numbers))

# q3
def question_3(store, customer):
    answer = []
    for i in customer:
        check = False
        for j in store:
            if i == j:
                check = True
        if check == True:
            answer.append('yes')
        else: answer.append('no')
    return answer

"""
store = [2,3,7,8,9]
customer = [7,5,9]
print(question_3(store, customer))
"""

# q4
def question_4(arr):
    new_arr = arr.copy()
    try: new_arr.remove(0)
    except: pass
    try: new_arr.remove(1)
    except: pass
    length = len(arr)
    if length == 2:
        min = np.min((new_arr))
        for i in range(2, min+1):
            if new_arr[0] % i == 0 and new_arr[1] % i == 0:
                return_answer = int((new_arr[0] * new_arr[1]) / i)
                return return_answer
            else: return new_arr[0] * new_arr[1]
    else:
        temp = question_4([new_arr[0], new_arr[1]])
        if len(new_arr) > 2:
            del new_arr[0]
            del new_arr[0]
            new_arr.append(temp)
            return question_4(new_arr)
        elif len(new_arr) == 2: return question_4(new_arr)
        else: return temp

arr = [2,6,8,14]
# arr = [1,2,3]
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# arr = [9, 10]
answer = question_4(arr)
print(answer)

# q5
def question_5(n, s):
    if s < 2:
        return -1
    s_2 = s // 2
    s_3 = s - s_2
    answer = [s_2, s_3]
    return answer

"""
n = 2
s = 1
answer = question_5(n, s)
print(answer)
"""

# q6
def question_6(arr):
    if len(arr) <= 1:
        return -1
    min = arr[0]
    for i in arr:
        if min > i:
            min = i
    new_arr = arr.copy()
    new_arr.remove(min)
    return new_arr

# arr = [4, 3, 2, 1]
# arr = [10]
# answer = question_6(arr)
# print(answer)

# q7
def question_7(arr):
    temp = arr[0]
    answer = []
    answer.append(temp)
    for i in arr:
        if temp == i:
            pass
        else:
            answer.append(i) 
            temp = i
    return answer

"""
arr = [1,1,3,3,0,1,1]
# arr = [4,4,4,3,3]
answer = question_7(arr)
print(answer)
"""