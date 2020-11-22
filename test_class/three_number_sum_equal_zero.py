

class Solution(object):
    """
    Write a Python class to find the three elements that sum to zero from a set of n real numbers
    """
    def get_three_numbers_sum_zero1(self, original_list):
        result_list = []
        length = len(original_list)
        for i in range(0, length - 2):
            for j in range(i + 1, length - 1):
                for k in range(j + 1, length):
                     if original_list[i] + original_list[j] +\
                             original_list[k] == 0:
                         result_list.append([original_list[i],
                                             original_list[j],
                                             original_list[k]])
                     else:
                         continue
        return result_list

    def get_three_numbers_sum_zero2(self, original_list):
        i, length, original_list = \
            0, len(original_list), sorted(original_list)
        result_list = list()
        while i < length - 2:
            j = i + 1
            k = length - 1
            while j < k:
                if original_list[i] + original_list[j] + original_list[k] > 0:
                    k -= 1
                elif original_list[i] + original_list[j] + original_list[k] < 0:
                    j += 1
                else:
                    result_list.append([original_list[i],
                                        original_list[j],
                                        original_list[k]])
                    j += 1
                    k -= 1
                    if j < k and original_list[j] == original_list[j - 1]:
                        j += 1
                    if j < k and original_list[k] == original_list[k + 1]:
                        k -= 1
            i += 1
            while i < length - 2 and original_list[i] == original_list[i - 1]:
                i += 1
        return result_list


if __name__ == '__main__':
    solution = Solution()
    # print(solution.get_three_numbers_sum_zero1(
    #     [-25, -10, -7, -3, 2, 4, 8, 10]))
    print(solution.get_three_numbers_sum_zero2(
        [-25, -10, -7, -3, 2, 4, 8, 10]))

