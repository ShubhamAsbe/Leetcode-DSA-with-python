class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        li=[]
        for i in range(0,32):
            li.append(pow(2,i))
        for i in li:
            if n==i:
                return True
        return False
