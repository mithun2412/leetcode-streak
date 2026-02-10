class Solution:
    def nofh(self, m, piles):
        ans = 0
        for i in piles:
            ans += (i + m - 1) // m   # ceil(i / m)
        return ans

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        k = r

        while l <= r:
            m = (l + r) // 2
            if self.nofh(m, piles) > h:
                l = m + 1
            else:
                k = m
                r = m - 1

        return k
