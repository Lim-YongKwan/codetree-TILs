import sys
INT_MAX = sys.maxsize

n = int(input())
arr = list(map(int, input().split()))
answer = INT_MAX

for i in range(1,n+1):
    sum_val = 0
    for j in range(n):
        sum_val += arr[j] * abs(j-i)
    answer = min(sum_val, answer)

print(answer)