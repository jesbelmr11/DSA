class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        else:
            y=str(x)[::-1]
            if str(x)==y:
                return True
            else:
                return False