def binarysearch(mylist,key):
    low=0
    high=len(mylist)-1
    while(low<=high):
        mid=(low+high)//2
        if key ==mylist[mid]:
            return mid
        elif key<mylist[mid]:
            high=mid-1
        else:
            low=mid+1
    return -1
n=int(input("Enter the range : "))
list=[]
for i in range(n):
    x=int(input("Enter the number : "))
    list.append(x)
list.sort()
# Display the sorted list
print("Sorted list:", list)
# Get the key to search
key = int(input("Enter the number to search: "))
# Perform binary search
index = binarysearch(list, key)
# Display the result
if index != -1:
    print(f"Element {key} found at index {index}.")
else:
    print(f"Element {key} not found in the list.")