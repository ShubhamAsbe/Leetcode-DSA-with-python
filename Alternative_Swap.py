size=int(input("Enter the size of the Array:"))
arr=[]

for i in range (0,size):
    element=int(input("Enter the Element:"))
    arr.append(element)

for i in range(0,size,2):
    if(i+1<size):
        arr[i],arr[i+1]=arr[i+1],arr[i]
print(arr)