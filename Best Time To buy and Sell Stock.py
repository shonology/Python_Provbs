class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p1 = prices[0]#initalizing initilal min stock value of list
        p2 = 0 #initializing max value to 0
        for price in prices[1:]:
            #each iteration finds min value and find its profit 
            p1 = min(p1, price)
            p2 = max(p2, price - p1)
        return p2 # returns profit 
        return 0 # returns if no profit found
