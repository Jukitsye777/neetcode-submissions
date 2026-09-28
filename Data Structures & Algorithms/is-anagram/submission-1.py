class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictionary_a = {}
        dictionary_b = {}

        if(len(s)!=len(t)):
            return False
        for i in range(len(s)):
            if (s[i] in dictionary_a):
                dictionary_a[s[i]] += 1
            else:
                dictionary_a[s[i]] = 1

        for i in range(len(t)):
            if(t[i] in dictionary_b ):
                dictionary_b[t[i]] += 1
            else:
                dictionary_b[t[i]] = 1

        if(dictionary_a == dictionary_b):
            return True
        
        return False

