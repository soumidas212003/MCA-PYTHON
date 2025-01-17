#Selection Sort
def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr
elements=[64,34,15,24,20,11]
print("Original list:",elements)
sorted_elements=selection_sort(elements)
print("Sorted list:",sorted_elements)    
        