'''
Given list is [2,3,6,6,5] . 
The maximum score is , second maximum is 6. Hence, we print 5 as the runner-up score.

Sample Input 0

5
2 3 6 6 5
Sample Output 0

5
'''

n=int(input()) 
arr=[]
while len(arr) < n:
    arr += list(map(int, input().split()))
arr=set(arr)
arr.remove(max(arr))
print(max(arr))
