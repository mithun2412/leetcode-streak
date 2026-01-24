class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Base cases
        if n == 1:
            return True          # 2⁰
        if n <= 0 or n % 2 != 0:
            return False         # negative, zero, or odd numbers

        # Recursive call
        return self.isPowerOfTwo(n // 2)
