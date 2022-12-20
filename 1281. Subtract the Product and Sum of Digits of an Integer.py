class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        sums=0
        pro=1
        while(n>0):
            i=n%10
            sums=sums+i
            pro=pro*i
            n=n//10
        return pro-sums