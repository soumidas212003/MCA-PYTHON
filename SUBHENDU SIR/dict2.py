#Write a python program to invert a dictionary i.e keys of a dictionary will be values in another dictionary and vice versa.
dic1={'Name':'Soumita','Roll':41,'Total':586}
dic2={}
for key,val in dic1.items():
    dic2[val]=key
print("The inverted Dictionary:",dic2)