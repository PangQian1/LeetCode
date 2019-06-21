class Solution:
    def longestPalindrome(self, s: str) -> str:  #->的含义定义返回类型，或者将返回值转换为该类型
        if(s.__len__() == 0):
            return ""

        strList = list(s)
        if(s.__len__() == 2 and strList[0] == strList[1]):
            return s

        r = 0
        s = 0
        maxLen = 1
        len = strList.__len__()
        for num in range(1, len-1):
            pde = 1
            i = num - 1
            j = num + 1
            while(i > -1 and j < len):
                if(strList[i] == strList[j]):
                    i -= 1
                    j += 1
                    pde += 2
                elif((strList[i] == strList[num] or strList[j] == strList[num]) and pde == 1):
                    pde += 1
                    if(strList[i] == strList[num]):
                        i -= 1
                    else:
                        j += 1
                    break
                else:
                    break
            if(pde > maxLen):
                maxLen = pde
                r = i + 1
                s = j - 1


        res = ''.join(strList[r:s+1])
        return res


s = Solution()
print(s.longestPalindrome("bb"))