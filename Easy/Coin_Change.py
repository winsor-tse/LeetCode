"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
"""

class Solution:
    """
    Time : O(n) n is the amount
    Space: O(n) n is the amount
    
    """
    
    def DFS(self, amount, coins, memo):
        if amount in memo:
            return memo[amount]
        if amount == 0:
            return 0
        if amount < 0:
            return float("inf")
        best = float("inf")
        for c in coins:
            best = min(best, 1+self.DFS(amount-c, coins, memo))
            memo[amount] = best
        return best

if __name__=="__main__":
    coins = [1,2,5]
    amount = 11
    memo = {}
    Sol = Solution()
    r = Sol.DFS(amount,coins, memo)
    if r == float("inf"):
        print("no Solution")
    else:
        print(r)


