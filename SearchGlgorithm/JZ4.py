from typing import List

"""
    二维数组中的查找
"""
class Solution:
    def Find(self , target: int, array: List[List[int]]) -> bool:
        b = False
        length = len(array)
        # 遍历每个一维数组，查看是否在里面。因为不能直接在二维数组in
        if length != 0:
            for i in range(length):
                if target in array[i]:
                    b = True
        return b