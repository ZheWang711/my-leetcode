__author__ = 'zhewang711'


class State:
    def __init__(self):
        self.state = 0  # whether have the stock
        self.profits = 0
        self.current = None

    def buy(self, price):
        if self.current is not None:
            raise ValueError("already have a stock")
        self.current = price
        self.state = 1

    def sell(self, price):
        if self.current is None:
            raise ValueError("cannot sell because haven't bought the stock")
        self.profits += (price - self.current)
        self.state = 0
        self.current = None

class AI:

    def __init__(self, prices, k):
        self.prices = prices
        self.person = State()
        self.A = [None for i in range(len(prices))] # 'h' -- hold; 'b' -- buy; 's' -- sell
        self.max_profit = 0
        self.max_k = k
        self.action = None

    def _decision(self, cur, k):

        if cur == len(self.prices):
            if self.max_profit < self.person.profits:
                self.max_profit = self.person.profits
                self.action = self.A.copy()
            return

        if self.person.state == 0:
            if k < self.max_k:
                self.A[cur] = 'b'
                self.person.buy(self.prices[cur])
                self._decision(cur + 1, k)
                self.person.sell(self.prices[cur])  # recover global variables

            # if the market is going to fall, not buy
            if cur + 1 < len(self.prices) and self.prices[cur] >= self.prices[cur + 1]:
                self.A[cur] = 'h'
                self._decision(cur + 1, k)
        else:
            # if the market is going to rise, not sell
            if cur + 1 < len(self.prices) and self.prices[cur] <= self.prices[cur + 1]:
                self.A[cur] = 'h'
                self._decision(cur + 1, k)

            self.A[cur] = 's'
            self.person.sell(self.prices[cur])
            self._decision(cur + 1, k + 1)
            self.person.buy(self.prices[cur])   # recover global variables

class Solution:

    def maxProfit(self, k, prices):
        t = AI(prices, k)
        t._decision(0, 0)
        self.record = t
        return t.max_profit

if __name__ == '__main__':
    a = Solution()
    print(a.maxProfit(4, [1, 2, 3, 4, 3, 2, 3, 4, 5, 4]))
    print(a.record.action)
