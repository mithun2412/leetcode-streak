class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""

        # Step 1: keep only letters and numbers
        for i in range(len(s)):
            ch = s[i]

            if "A" <= ch <= "Z":
                clean += chr(ord(ch) + 32)   # convert to lowercase
            elif "a" <= ch <= "z":
                clean += ch
            elif "0" <= ch <= "9":
                clean += ch

        # Step 2: check palindrome
        i = 0
        j = len(clean) - 1

        while i < j:
            if clean[i] != clean[j]:
                return False
            i += 1
            j -= 1

        return True
