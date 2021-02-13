'''
122. Best Time to Buy and Sell Stock II
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

Say you have an array prices for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like 
(i.e., buy one and sell one share of the stock multiple times).
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = 0
        
        if len(prices) < 2:
            return p
        
        for i in range(1,len(prices)):
            if prices[i-1] < prices[i]:
                p += prices[i] - prices[i-1]
            
        return p
