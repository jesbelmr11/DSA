class Solution(object):
    def plusOne(self, digits):

        arr=[]
        numstr=""
        for i in range(len(digits)):
            a=str(digits[i])
            numstr=numstr+a
        
        num=int(numstr)
        ans=num+1

        for j in str(ans):
            arr.append(int(j))
        
        return arr
