class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen=[]
        num=n

        def sq(k):
            sum=0
            string=str(k)

            for i in string:
                sum=sum+int(i)**2
            return sum

        while num!=1:
            if num in seen:
                return False
            
            seen.append(num)
            p=sq(num)
            num=p
        return True
