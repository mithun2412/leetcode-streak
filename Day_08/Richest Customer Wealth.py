class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        maxsum = 0
        for i in range(len(accounts)):
            sum = 0
            for j in range(len(accounts[i])):
                sum +=accounts[i][j]

            if maxsum<sum:
                maxsum=sum
        return maxsum
                