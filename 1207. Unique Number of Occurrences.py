class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr.sort()
        count=[]
        flag=0
        if len(arr)==2:
            if arr[0]!=arr[1]:
                return False
        for i in range(0,len(arr)-1):
            if arr[i]==arr[i+1]:
                flag+=1
            if(arr[i]!=arr[i+1]):
                if flag not in count:
                    count.append(flag)
                    flag=0
                else:
                    return False
        return True  