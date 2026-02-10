class Solution:
    def reverseWords(self, s: str) -> str:
        
        nword = ""
        nsen = ""

        # add a space at the end to process last word
        s = s + " "

        for i in range(len(s)):
            if s[i] != " ":
                nword += s[i]
            elif nword != "":
                if nsen == "":
                    nsen = nword
                else:
                    nsen = nword + " " + nsen
                nword = ""

        return nsen

