class Solution:
    def appendCharacters(self, s: str, t: str) -> int:


        i,j = 0,0
        size_s = len(s)
        size_t = len(t)
        limit = size_t
        count = 0
        left_end = 0

        while(i<size_t):

            while(j<size_s):
                if(t[i] == s[j]):
                    count += 1
                    j+=1
                    break
                j+=1
                
            if(j==size_s):
                return limit - count
                
            i+=1


        return limit - count

        