'''
解题思路
将输入的字符串解析为为字符list——oriList
给定一个list--indexList，该list和oriList下标值一一对应，存储内容为该index对应字符所属Z字形中的行数
将相同行的字符拼接成字符串，然后将所有拼接好的字符串按照行数拼接成结果字符串即可

需要考虑的特殊情况：numRows=1的情况
'''

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if(numRows == 1):
            return s

        #第一个list，内容为输入字符串的字符列表
        oriList = list(s)
        #第二个list，记录了划分为Z字形后，每个字符对应的行数，下标值与第一个list完全对应
        indexList = []
        #第三个list，将所有字符按照划分为Z字形后的行数，从前至后，同行的拼接到一起，该list长度即为numRows
        resList = []
        #初始化
        for num in range(0, numRows + 1):
            resList.insert(num, "")

        len = oriList.__len__()
        oneRound = 2 * numRows - 2 #一轮包括多少字符

        for num in range(0, len):
            if(num < numRows):
                indexList.insert(num, num + 1)
            elif(num < oneRound):
                indexList.insert(num, 2*numRows - num - 1)
            else:
                indexList.insert(num, indexList[num - oneRound])

        #遍历indexList，将位于同行的字符拼接成字符串，写入resList
        for num in range(0, len):
            index = indexList[num] #代表字符所在行数
            resList[index] += oriList[num]

        res = "".join(resList)
        return res


s = Solution()
print(s.convert("ABC", 2))