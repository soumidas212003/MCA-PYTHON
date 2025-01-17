#Write a python program to show how to iterate through a dictionary
student={'Roll':41,'Name':'Soumita','Marks':78}
print("Student: ",student)
for key in student.keys():
    print("Keys are",key)
for val in student.values():
    print("values are",val)