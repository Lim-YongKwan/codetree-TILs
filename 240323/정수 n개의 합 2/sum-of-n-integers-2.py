n, k = map(int, input().split())
arr = [0] + list(map(int, input().split()))
sum_A = [0] * (n+1)
answer = [0] * (n-k+1)

for i in range(n):
    sum_A[i] = sum_A[i-1] + arr[i]

for j in range(n-k+1):
    answer[j] = sum_A[j+k] - sum_A[j]

print(max(answer))