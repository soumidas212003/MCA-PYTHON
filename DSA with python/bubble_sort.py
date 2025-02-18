def bubble_sort(list):
    n=len(list)
    for i in range(n-1):
        for j in range(n-i-1):
            if list[j]>list[j+1]:
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp
    return list
n=int(input("Enter the size: "))
list=[]
for i in range(n):
    ele=int(input("Enter the number: "))
    list.append(ele)
print(list)
print("After sort list is: ",bubble_sort(list))