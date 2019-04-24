# -*- coding:utf-8 -*-
'''
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''

class Solution:
    # array 二维列表
    def find_simple(self, target, array):
       for arr in array:
        if target in arr:
            return True
        return False
    
    def find_normal(self, target, array):
        row = len(array)
        if row == 0:
            return False
        
        col = len(array[0]) - 1
        i, j = row - 1, 0
        
        while i >= 0:
            while j <= col:
                val = array[i][j]
                if target > val:
                    if j == col:
                        return False
                    j += 1
                elif target < val:
                    break
                else:
                    return True
            i -= 1
            
        return False


test_arr = [[1,4,7], [2,5,8], [3,6,9]]
s = Solution()
print(s.find_normal(20, test_arr))
