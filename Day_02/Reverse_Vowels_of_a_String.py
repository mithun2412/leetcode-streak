class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "AEIOUaeiou"
        vowel_list = []
        result = ""

        # Step 1: collect vowels
        for ch in s:
            if ch in vowels:
                vowel_list.append(ch)

        # Step 2: reverse vowels
        vowel_list.reverse()

        # Step 3: rebuild string
        for ch in s:
            if ch in vowels:
                result += vowel_list.pop(0)
            else:
                result += ch

        return result

