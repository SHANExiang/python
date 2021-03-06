
# 输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。
#

class Solution:
    def getLeastNumbers(self, arr, k):
        def quick_sort(arr, left, right):
            if right <= left:
                return
            i, j = left, right
            while i < j:
                while i < j and arr[j] >= arr[left]:
                    j -= 1
                while i < j and arr[i] <= arr[left]:
                    i += 1
                arr[i], arr[j] = arr[j], arr[i]
            arr[i], arr[left] = arr[left], arr[i]
            quick_sort(arr, left, i - 1)
            quick_sort(arr, i + 1, right)
        quick_sort(arr, 0, len(arr) - 1)
        return arr[:k]


if __name__ == "__main__":
    solution = Solution()
    print(solution.getLeastNumbers([0, 1, 2, 1, 5, 4, 3, 2, 0], 4))