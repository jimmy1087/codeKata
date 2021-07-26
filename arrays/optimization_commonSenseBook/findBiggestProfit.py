# You’re working on some more stock-prediction software. The function you’re writing accepts an array of predicted prices for a particular stock over the course of time.
# For example, this array of seven prices:
#​ 	[10, 7, 5, 8, 11, 2, 6]
# predicts that a given stock will have these prices over the next seven days. (On Day 1, the stock will close at $10; on Day 2, the stock will close at $7; and so on.)
# Your function should calculate the greatest profit that could be made from a single “buy” transaction followed by a single “sell” transaction.
# In the previous example, the most money could be made if we bought the stock when it was worth $5 and sold it when it was worth $11. This yields a profit of $6 per share.


def findBiggestProfit(array):

    buy_price = array[0]
    greatest_profit = 0

    for price in array:

        potential_profit = price - buy_price

        if price < buy_price:
            buy_price = price

        if potential_profit > greatest_profit:
            greatest_profit = potential_profit

    return  greatest_profit

a = [10, 7, 5, 8, 11, 2, 6]
print(findBiggestProfit(a))
a = [3, 2, 10, 5, 8, 11, 1]
print(findBiggestProfit(a))
a = [3, 2, 11, 1, 2, 11]
print(findBiggestProfit(a))
        
            