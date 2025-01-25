'''
Task
Given an integer,n, and n space-separated integers as input, create a tuple, t, of those n intergers.Then compute and print the result of hash(t).

Sample Input 0

2
1 2
Sample Output 0

3713081631934410656
'''

n=int(input())
t=tuple(map(int, input().split()))
print(hash(t))