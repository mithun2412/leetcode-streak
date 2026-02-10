class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        temp = num
        while num >0:
            rem = num%10
            if temp  % rem ==0:
                count+=1
            num//=10
        return count
