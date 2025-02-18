def bubble_sort(list):
    n=len(list)
    for i in range(n-1):
        flag=False
        for j in range(n-i-1):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
                flag=True
        if flag==False:
            break
    return list
n=int(input("Enter the size: "))
list=[]
for i in range(n):
    ele=int(input("Enter the number: "))
    list.append(ele)
print("Before sort list is: ",list)
print("After sort list is: ",bubble_sort(list))

