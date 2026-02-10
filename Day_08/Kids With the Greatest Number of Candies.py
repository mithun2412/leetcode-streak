class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n = max(candies)
        summ =0
        l1=[]
        for i in range(len(candies)):
            if candies[i]+extraCandies >= n:
                l1.append(True)
            else:
                l1.append(False)
        return l1