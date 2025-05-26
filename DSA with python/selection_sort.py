def selection_sort(list):
    n=len(list)
    for i in range(n-1):
        min=i
        for j in range(i+1,n):
            if list[j]<list[min]:
                min=j
        if min != i:
            list[i],list[min]=list[min],list[i]
    return list
n=int(input("Enter the size: "))
list=[]
for i in range(n):
    ele=int(input("Enter the number: "))
    list.append(ele)
print(list)
print("After sort list is: ",selection_sort(list))