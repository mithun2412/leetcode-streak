class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        result = ""

        for i in range(len(strs[0])):        # go character by character
            current_char = strs[0][i]

            for s in strs:                   # check this char in all strings
                if i == len(s) or s[i] != current_char:
                    return result            # stop immediately

            result += current_char           # add char if all matched

        return result

#Time Complexity: O(S) where S is the sum of all characters in all strings.
#Space Complexity: O(1)