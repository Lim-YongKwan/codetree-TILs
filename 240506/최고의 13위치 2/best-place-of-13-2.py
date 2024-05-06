n = int(input())
arr = [ list(map(int, input().split())) for _ in range(n)]

max_sum = 0
sum_val = 0
second_max = 0

for i in range(n):
    for j in range(n-2):
        sum_val = arr[i][j] + arr[i][j+1] + arr[i][j+2]
        max_sum = max(max_sum, sum_val)

for i in range(n):
    for j in range(n-2):
        sum_val = arr[i][j]+arr[i][j+1]+arr[i][j+2]
        if sum_val != max_sum:
            second_max = max(second_max, sum_val)

print(max_sum+second_max)