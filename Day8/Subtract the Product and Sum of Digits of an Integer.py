class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        pro=1
        sum=0
        res = 0
        temp = n
        while n>0:
            rem = n %10
            pro = pro*rem
            sum +=rem
            n//=10
        res = pro - sum
        return res
            
