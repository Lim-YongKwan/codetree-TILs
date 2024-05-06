n = int(input())
arr = [ list(map(int, input().split())) for _ in range(n)]

max_sum = 0
sum_val = 0
sum_val2 = 0
total_sum = 0

for i in range(n):
    for j in range(n-2):
        sum_val = arr[i][j] + arr[i][j+1] + arr[i][j+2]
        second_max = 0
        for k in range(n):
            for l in range(n-2):
                if i == k:
                    if l > j+2 and l < n-2:
                        sum_val2 = arr[k][l] + arr[k][l+1]+arr[k][l+2]
                    else:
                        sum_val2 = 0
                else:
                    sum_val2 = arr[k][l] + arr[k][l+1] + arr[k][l+2]
                second_max = max(second_max, sum_val2)
        total_sum = sum_val + second_max
        max_sum = max(max_sum, total_sum)
        
print(max_sum)