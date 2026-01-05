class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        result = ""

        for i in range(len(strs[0])):       
            current_char = strs[0][i]

            for s in strs:                   
                if i == len(s) or s[i] != current_char:
                    return result           

            result += current_char           
        return result

#Time Complexity: O(S) where S is the sum of all characters in all strings.
#Space Complexity: O(1)