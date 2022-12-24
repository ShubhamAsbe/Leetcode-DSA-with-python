def findUnique(arr, n) :
    #Your code goes here
    arr.sort()
    for i in range(0,n,2):
        if(i+1<n):
            if(arr[i]!=arr[i+1]):
                break
    return arr[i]