class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        minprice=prices[0]
        maxprice=prices[0]
        profit=0

        for i in range(1,len(prices)):
            if prices[i]<minprice:
                minprice=prices[i]
                maxprice=prices[i]
            else:
                if prices[i]>maxprice:
                    maxprice=prices[i]
                
                if maxprice-minprice>profit:
                    profit=maxprice-minprice
        return profit

               




        