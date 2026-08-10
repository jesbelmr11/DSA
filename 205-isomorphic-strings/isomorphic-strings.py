class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        dict1,dict2={},{}

        if len(s)!=len(t):
            return False
        else:
            for i in range(len(s)):
                a=s[i]
                b=t[i]

                if((a in dict1 and dict1[a]!=b) or (b in dict2 and dict2[b]!=a)):
                    return False
                else:
                    dict1[a]=b
                    dict2[b]=a
            return True
