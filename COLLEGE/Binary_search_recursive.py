# Binary Search(Recursive Way)

def bin_search(list,key,low,high):
    if low<=high:
        mid=(low+high)//2
        if key==list[mid]:
            print("The",key,"is present in the",mid,"th index")
        elif key > list [mid]:
            return bin_search(list,key,mid+1,high)
        else:
            return bin_search (list,key,low,mid-1)
    else:
        print("The",key,"is not present in the list")
num_list=[]
for i in range(1,11):
    num_list.append(i)
print("Enter the key to be searched")
key=int(input("Enter The key value between 1 and 10: "))
bin_search(num_list,key,0,len(num_list)-1)