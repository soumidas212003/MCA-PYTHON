def partitionlist(list,left,right):
    loc=left
    while True:
        while list[loc]<=list[right] and loc!=right:
            right-=1
        if loc==right:
            break
        elif list[loc]>list[right]:
            list[loc],list[right]=list[right],list[loc]
            loc=right
        while list[loc]>=list[left] and loc!=left:
            left+=1
        if loc==left:
            break
        elif list[loc]<list[left]:
            list[loc],list[left]=list[left],list[loc]
            loc=left
    return loc
def quicksort(list,left,right):
    if left<right:
        loc=partitionlist(list,left,right)
        quicksort(list,left,loc-1)
        quicksort(list,loc+1,right)
n=int(input("Enter the size: "))
list=[]
for i in range(n):
    ele=int(input("Enter the number: "))
    list.append(ele)
print(list)
quicksort(list,0,n-1)
print(list  )