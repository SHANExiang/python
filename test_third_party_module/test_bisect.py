import bisect


def insert_into_left_right():
    original_list = [1, 2, 4, 7]
    print(bisect.bisect_left(original_list, 3))
    print(bisect.bisect_right(original_list, 3))


# insert_into_left_right()
# 2
# 2


'''
Write a Python program to insert items into a list in sorted order. 
Expected Output:
Original List:
[25, 45, 36, 47, 69, 48, 68, 78, 14, 36]
Sorted List:
[14, 25, 36, 36, 45, 47, 48, 68, 69, 78]
'''


def insert_element_in_original_order():
    original_list = [25, 45, 36, 47, 69, 48, 68, 78, 14, 36]
    result_list = list()
    print('Original List:')
    print(original_list)
    print("Sorted List:")
    for ele in original_list:
        bisect.insort(result_list, ele)
    print(result_list)


insert_element_in_original_order()
