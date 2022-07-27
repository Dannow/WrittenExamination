from typing import List

"""
    数字在升序数组中出现的次数
"""
class Solution:
    def GetNumberOfK(self , data: List[int], k: int) -> int:
        count = 0
        length = len(data)
        if length != 0 :
            # 遍历数组，统计次数
            for i in range(length):
                if data[i] == k:
                    count += 1
        return count