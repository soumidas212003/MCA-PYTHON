# write a python program to find the frequency of each letter in a string
str1=input("Enter any string :")
freq={}
for ch in str1:
    freq[ch]=freq.get(ch,0)+1
print("Frequency of each letter:")
for key,val in freq.items():
    print(key,"=",val)