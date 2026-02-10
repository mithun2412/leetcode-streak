class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        for i in range(len(s)):
            if s[i] not in freq:
                freq[s[i]]=1 
            else:
                freq[s[i]] +=1
        for str1 in t:
            if str1 not in freq:
                return False
            else:
                freq[str1]-=1
        for val in freq.values():
            if val != 0:
                return False
        return True