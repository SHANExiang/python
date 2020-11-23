
"""
Write a Python program for binary search. Go to the editor
Binary Search : In computer science, a binary search or half-interval search
 algorithm finds the position of a target value within a sorted array.
 The binary search algorithm can be classified
 as a dichotomies divide-and-conquer search algorithm and executes in logarithmic time.
Test Data :
binary_search([1,2,3,5,8], 6) -> False
binary_search([1,2,3,5,8,10,14,15], 5) -> True
"""


def binary_search(original_list, target):
    left = 0
    right = len(original_list) - 1
    if target > original_list[right] or target < original_list[left]:
        return False
    while left <= right:
        middle = int((left + right)/2)
        if target > original_list[middle]:
            left = middle + 1
        elif target < original_list[middle]:
            right = middle - 1
        else:
            return True
    return False


# print(binary_search([1, 2, 3, 5, 6, 8], 6))

"""
Write a Python program for binary search for an ordered list. 
Test Data :
Ordered_binary_Search([0, 1, 3, 8, 14, 18, 19, 34, 52], 3) -> True
Ordered_binary_Search([0, 1, 3, 8, 14, 18, 19, 34, 52], 17) -> False
"""


def ordered_binary_search(ordered_list, target):
    if len(ordered_list) == 0:
        return False
    else:
        middle = len(ordered_list)//2
        if ordered_list[middle] == target:
            return True
        else:
            if target < ordered_list[middle]:
                return binary_search(ordered_list[:middle], target)
            else:
                return binary_search(ordered_list[middle+1:], target)


print(ordered_binary_search([0, 1, 3, 8, 14, 18, 19, 34, 52], 3))
