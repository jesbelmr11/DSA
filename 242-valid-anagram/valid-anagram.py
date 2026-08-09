class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        freqs={}

        for i in s:
            if i in freqs:
                freqs[i]=freqs[i]+1
            else:
                freqs[i]=1

        freqt={}

        for i in t:
            if i in freqt:
                freqt[i]=freqt[i]+1
            else:
                freqt[i]=1
        
        if freqs==freqt:
            return True
        else:
            return False
        