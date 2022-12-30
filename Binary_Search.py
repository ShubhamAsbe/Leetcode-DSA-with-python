def binarySearch(arr,key):
    start=0
    end=len(arr)-1
    mid=(start+end)//2
    print(mid)
    while(start<=end):
        if(arr[mid]==key):
            return mid
        elif(arr[mid]<key):
            start=mid+1
        else:
            end=mid-1
        mid=(start+end)//2
    return -1


li=[1,3,5,7,9,11,13,15]
binarySearch(li,5)
