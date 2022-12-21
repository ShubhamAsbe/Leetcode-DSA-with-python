class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        q=0
        if(x==0):
            return 0
        elif(x>0):
            s=str(x)
            s=s[::-1]
            q=int(s)
        else:
            n=str(x)
            n=n[1:]
            n=n[::-1]
            f="-"+n
            q=int(f)
        if(q>(pow(2,31)-1) or q<-pow(2,31)):
            return 0
        else:
            return q


        