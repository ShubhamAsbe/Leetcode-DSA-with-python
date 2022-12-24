def findDuplicate(arr):
    # Write your code here
    unique=[]
    for i in arr:
        if i not in unique:
            unique.append(i)
        else:
            return i
      
            

    pass
