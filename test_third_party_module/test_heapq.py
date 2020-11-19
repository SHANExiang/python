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


