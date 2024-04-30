n = int(input())
arr = list(map(int, input().split()))
sum_val = 0
max_sum = 0

for i in range(n):
    for j in range(1,n):
        if i==j or i+1 == j or i-1 == j:
            continue
        sum_val = arr[i] + arr[j]
        max_sum = max(max_sum, sum_val)
print(max_sum)