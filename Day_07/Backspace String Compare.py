class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1=[]
        stack2=[]
        
        for i in range(len(s)):
            if s[i]!="#":
                stack1.append(s[i])
            elif len(stack1)>0:
                stack1.pop()
        for i in range(len(t)):
            if t[i]!="#":
                stack2.append(t[i])
            elif len(stack2)>0:
                stack2.pop()
        return stack1==stack2