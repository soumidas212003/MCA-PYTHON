#Write a python program to merge two python dictionaries into one 
dic1={1:1,3:9,5:25}
dic2={2:4,4:16,6:36}
dic3={}
for key,val in dic1.items():
    dic3[key]=val
for key,val in dic2.items():
    dic3[key]=val
print("After merging two dictionaries",dic3)