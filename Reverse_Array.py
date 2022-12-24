size=int(input("Enter the size of the Array:"))
arr=[]

for i in range (0,size):
    element=int(input("Enter the Element:"))
    arr.append(element)
rev=[]

for i in range(len(arr)-1,-1,-1):
    rev.append(arr[i])

print("Reversed Array is:",rev)