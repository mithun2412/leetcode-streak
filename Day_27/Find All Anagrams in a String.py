class Solution:
    def findAnagrams(self, s: str, p: str):
        if len(p) > len(s):
            return []

        count_p = [0] * 26
        count_s = [0] * 26

        for i in range(len(p)):
            count_p[ord(p[i]) - ord('a')] += 1
            count_s[ord(s[i]) - ord('a')] += 1

        res = []

        if count_p == count_s:
            res.append(0)

        left = 0

        for right in range(len(p), len(s)):
            count_s[ord(s[right]) - ord('a')] += 1
            count_s[ord(s[left]) - ord('a')] -= 1
            left += 1

            if count_s == count_p:
                res.append(left)

        return res