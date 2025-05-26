def mergelist(list,lst,lend,rst,rend):
    temp=[]
    i=lst
    j=rst
    while i<=lend and j<=rend:
        if list[i]<list[j]:
            temp.append(list[i])
            i+=1
        else:
            temp.append(list[j])
            j+=1
    while i<=lend:
        temp.append(list[i])
        i+=1
    while j<=rend:
        temp.append(list[j])
        j+=1
    j=0
    for i in range(lst,rend+1):
        list[i]=temp[j]
        j+=1
def mergesort(list,left,right):
    if left<right:
        mid=(left+right)//2
        mergesort(list,left,mid)
        mergesort(list,mid+1,right)
        mergelist(list,left,mid,mid+1,right)
n=int(input("Enter the size: "))
list=[]
for i in range(n):
    ele=int(input("Enter the number: "))
    list.append(ele)
print(list)
mergesort(list,0,n-1)
print(list)