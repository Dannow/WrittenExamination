from typing import List

"""
    字符串的排列(全排列)
"""
class Solution:
    # step：步数；s：题目给的字符串；cur：排序好的字符串；ans：set集合用来存储排序好的字符串；book：标志位
    def dfs(self, step, s, cur, ans, book):
        # 递归边界，当获得一个排好序的数组，则返回上一层
        if step == len(s):
            # 把排好序的字符串加入到Set集合中，用set集合：题目中会包含重复的字母
            ans.add(cur)
            return

        # 遍历字符串长度
        for i in range(len(s)):
            # 判断当前位置字符有无被使用
            if (book[i] == 0):
                book[i] = 1     # 使用第i个字符
                cur += s[i]     # 插入到cur的最后一个位置
                # 递归下一层
                self.dfs(step + 1, s, cur, ans, book)
                cur = cur[:-1]  # 还原上一层的字符排序，即把最后一个位置弹出
                book[i] = 0     # 还原book


    def Permutation(self, str: str) -> List[str]:
        # 如果为空，直接返回
        if str == "":
            return
        # set集合用来存储排序好的字符串，因为题目中会包含重复的字母，排出来会有重复的值
        ans = set()
        cur = ""
        # 标记数组，初始化为0，大小为字符串长度
        book = [0 for _ in range(len(str))]
        self.dfs(0, str, cur, ans, book)
        # 把set转换为list返回
        return list(ans)