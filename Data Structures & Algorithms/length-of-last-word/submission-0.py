class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        sum = 0
        flag = 0

        for i in range(len(s)-1,-1,-1):
            if s[i] != " ":
                flag = 1
                sum+=1
            elif s[i] == " " and flag == 1:
                return sum
            


        return sum
        