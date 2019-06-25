'''
解题思路
共分为三种情况：①字符串为空串；②字符串包括最长回文子串长度为单数；③字符串包括最长回文子串长度为双数
①空串直接返回空串即可；
②单数时，遍历每一项，以该项为中心，比较左右等距离字符是否一致，找出最长回文子串
③双数时，遍历每一项，向右对称，没有中心项，找出最长回文子串。（注意，不能仅遍历左半部分，因为回文子串长度很可能不够总长的一半）
④选出以上各种情况最长子串，返回
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:  #->的含义定义返回类型，或者将返回值转换为该类型
        #长度为空的回文串
        if(s.__len__() == 0):
            return ""

        strList = list(s)

        r = 0
        s = 0
        maxLen = 1
        len = strList.__len__()

        #长度为双数的回文串
        for num in range(0, len):
            pde = 0
            i = num
            j = num + 1
            while(i > -1 and j < len):
                if(strList[i] == strList[j]):
                    pde += 2
                    i -= 1
                    j += 1
                else:
                    break
            if(maxLen < pde):
                maxLen = pde
                r = i + 1
                s = j - 1

        #长度为单数的回文串
        for num in range(1, len-1):
            pde = 1
            i = num - 1
            j = num + 1
            while(i > -1 and j < len):
                if(strList[i] == strList[j]):
                    i -= 1
                    j += 1
                    pde += 2
                else:
                    break
            if(pde > maxLen):
                maxLen = pde
                r = i + 1
                s = j - 1


        res = ''.join(strList[r:s+1])
        return res


s = Solution()
print(s.longestPalindrome("iptmykvjanwiihepqhzupneckpzomgvzmyoybzfynybpfybngttozprjbupciuinpzryritfmyxyppxigitnemanreexcpwscvcwddnfjswgprabdggbgcillisyoskdodzlpbltefiz"))