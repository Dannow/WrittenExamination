from typing import List

"""
    旋转数组的最小数字
"""
class Solution:
    '''
        冒泡排序
    '''
    # def minNumberInRotateArray(self , rotateArray: List[int]) -> int:
    #     for i in range(len(rotateArray) - 1):
    #         for j in range(len(rotateArray) - 1 - i):
    #             if rotateArray[j] > rotateArray[j + 1]:
    #                 temp = rotateArray[j]
    #                 rotateArray[j] = rotateArray[j + 1]
    #                 rotateArray[j + 1] = temp
    #     return rotateArray[0]

    # '''
    #     快速排序
    # '''
    # def quick_sort(self, s: List[int], left: int, right: int):
    #     if left < right:
    #         i = left
    #         j = right
    #         x = s[left]    # s[l]即s[i]就是第一个坑
    #         while i < j:
    #             # 从右向左找小于x的数来填s[i]
    #             while i < j and x <= s[j]:
    #                 j -= 1
    #             if i < j:
    #                 s[i] = s[j]     # 将s[j]填到s[i]中，s[j]就形成了一个新的坑
    #                 i += 1
    #             # 从左向右找大于或等于x的数来填s[j]
    #             while i < j and x > s[i]:
    #                 i += 1
    #             if i < j:
    #                 s[j] = s[i]     # 将s[i]填到s[j]中，s[i]就形成了一个新的坑
    #                 j -= 1
    #         # 退出时，i等于j。将x填到这个坑中。
    #         s[i] = x
    #         self.quick_sort(s, left, i-1)
    #         self.quick_sort(s, i + 1, right)
    #     return s
    #
    # def minNumberInRotateArray(self, rotateArray: List[int]) -> int:
    #     s = self.quick_sort(rotateArray, 0, len(rotateArray)-1)
    #     return s[0]

    def minNumberInRotateArray(self, rotateArray: List[int]) -> int:
        min_num = rotateArray[0]
        # 从头往尾找最小值
        for i in range(len(rotateArray)):
            if min_num > rotateArray[i]:
                min_num = rotateArray[i]
        return min_num


