class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 1
        res=0
        base=1

        while(n>0):
            if(n&1==0):
                res+=base
            n>>=1
            base<<=1
        return res

