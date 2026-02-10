class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi=-10**9
        mini=10**9
        for i in prices:
            if i<mini:
                mini=i
            if i-mini>maxi:
                maxi=i-mini
        

        return maxi

