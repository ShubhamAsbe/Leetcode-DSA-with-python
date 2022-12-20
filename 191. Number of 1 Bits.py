class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        one=0
        while(n>0):
            if(n&1):
                one=one+1
            n=n>>1
        return one