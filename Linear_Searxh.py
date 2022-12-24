size=int(input("Enter the size of the Array:"))
arr=[]
flag=0
for i in range (0,size):
    element=int(input("Enter the Element:"))
    arr.append(element)

key=int(input("Enter the key you want to search in the Array:"))
for i in range(0,size):
    if(key==arr[i]):
        flag=1
        break;

if flag==1:
    print("Element found on index:",i)
else:
    print("Element Not Found")