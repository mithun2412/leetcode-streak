class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.findpow(x, -n)
        return self.findpow(x, n)

    def findpow(self, x, n):
        if n == 0:
            return 1

        half = self.findpow(x, n // 2)

        if n % 2 == 0:
            return half * half
        else:
            return half * half * x
