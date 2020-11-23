

"""
Write a Python program to sort a list of elements using the selection sort algorithm.
Note : The selection sort improves on the bubble sort
by making only one exchange for every pass through the list.
Sample Data: [14,46,43,27,57,41,45,21,70]
Expected Result: [14, 21, 27, 41, 43, 45, 46, 57, 70]
"""


def selection_sort(original_list):
    for i in range(len(original_list) - 1, 0, -1):
        max_index = 0
        for j in range(1, i + 1):
            if original_list[j] > original_list[max_index]:
                max_index = j
        temp = original_list[i]
        original_list[i] = original_list[max_index]
        original_list[max_index] = temp
    return original_list


print(selection_sort([14,46,43,27,57,41,45,21,70]))




