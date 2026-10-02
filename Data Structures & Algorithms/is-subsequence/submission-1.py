class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        size_s = len(s)
        size_t = len(t)

        limit = size_s
        count = 0

        if(size_t<size_s):
            return False
        i,j = 0,0
        while(i<size_s):
            while(j<size_t):
                if(s[i] == t[j]):
                    count+=1
                    j+=1
                    break
                j+=1
            i+=1

        if(count == limit):
            return True

        return False
        