class Solution:
    def sortstring(self,s):
        s1=list(s)
        s1.sort()
        return "".join(s1)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict={}
        for i in strs:
            key = self.sortstring(i)
            if key in dict:
                dict[key].append(i)
            else:
                dict[key]=[i]
        return list(dict.values())
