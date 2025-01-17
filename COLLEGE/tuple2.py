#Write a python program to count the tuples in a list
tup1=[10,(2,1),(3,3),'Hi',[2,3,7],(10,19),{5,6,7}]
count=0
for i in tup1:
    if type(i)==tuple:
        count=count+1
print(f"Total no of tuples in the list are {count}")