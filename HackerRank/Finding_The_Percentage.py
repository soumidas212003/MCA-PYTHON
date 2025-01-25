'''
Input
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

Output(average)
56.00
'''

n = int(input())
my_dict = {}
for i in range(n):
    key, *value = input().split()
    value = list(map(float,value))
    my_dict[key] = value

query_name=input()
count=0
if query_name in my_dict:
    values = my_dict[query_name]
    avg = sum(values) / len(values)
    print(f"{avg:.2f}")
