import heapq


# print(heapq.nlargest(3, [1, 2, 3, 4]))  # 获得列表的最大的3个元素；
# print(heapq.nsmallest(3, [1, 2, 3, 4]))  # 获得列表的最小的3个元素；
# print(heapq.nlargest(3, {1: 'a', 2: 'b', 3: 'c', 4: 'd'})) # 获得字典的最大的3个键；


# ****************************************************************************
'''
Write a Python program to implement a heapsort by pushing all values onto a heap 
and then popping off the smallest values one at a time.
'''


def heap_sort(iterable_obj):
    res = []
    for obj in iterable_obj:
        heapq.heappush(res, obj)
    # for i in range(len(res)):
    #     print(heapq.heappop(res), end=' ')
    return [heapq.heappop(res) for i in range(len(res))]


# print(heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# ****************************************************************************
'''
Write a Python program to push three items into a heap and 
return the smallest item from the heap. 
Also Pop and return the smallest item from the heap. Go to the editor
Expected Output:
Items in the heap:
('V', 1)
('V', 3)
('V', 2)
----------------------
The smallest item in the heap:
('V', 1)
----------------------
Pop the smallest item in the heap:
('V', 2)
('V', 3)
'''


def pop_heap():
    original_list = [('V', 3), ('V', 2), ('V', 1)]
    heap_list = list()
    for ele in original_list:
        heapq.heappush(heap_list, ele)
    print('Item in the heap:')
    for x in heap_list:
        print(x)
    print('--------------------------')
    print("The smallest item in the heap:")
    print(heapq.heappop(heap_list))
    print('--------------------------')
    print('Pop the smallest item in the heap:')
    for x in heap_list:
        print(x)


# pop_heap()

'''
Write a Python program to push an item on the heap, then pop and 
return the smallest item from the heap. 
Items in the heap:
('V', 1)
('V', 3)
('V', 2)
----------------------
Using heappushpop push item on the heap and return the smallest item.
('V', 2)
('V', 3)
('V', 6)
'''


def test_heappushpop():
    heap_list = []
    heapq.heappush(heap_list, ('V', 3))
    heapq.heappush(heap_list, ('V', 2))
    heapq.heappush(heap_list, ('V', 1))
    print('Item in the heap:')
    for ele in heap_list:
        print(ele)
    print('-------------------------------')
    print('Using heappushpop push item on the heap and return the smallest item.')
    heapq.heappushpop(heap_list, ('V', 6))
    for x in heap_list:
        print(x)


# test_heappushpop()

