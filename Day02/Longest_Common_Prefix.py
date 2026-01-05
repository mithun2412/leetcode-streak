from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
    
        prefix = strs[0]
    
        for word in strs[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
    
        return prefix

#Time Complexity: O(S) where S is the sum of all characters in all strings.
#Space Complexity: O(1)