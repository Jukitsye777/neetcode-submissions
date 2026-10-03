class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0;
        start = 0
        end = 0
        for i in range(len(s)-1,-1,-1):
            if(s[i] == ' '):
                if(start == 1):
                    return count
                count = 0
                continue
            start = 1
            count += 1
        return count
        