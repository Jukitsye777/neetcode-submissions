class Solution:
    def scoreOfString(self, s: str) -> int:
        sum = 0
        for i in range(0,len(s)-1,1):
            diff = abs(ord(s[i]) - ord(s[i+1]))
            sum += diff
        
        return sum
