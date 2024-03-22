n, k = map(int, input().split())
arr = [0] + list(map(int, input().split()))

sum_A = [0] * (n+1)
for i in range(5,0+k-1,-1):
    #print(i)
    for j in range(k):
        sum_A[i] += arr[i-j]

print(max(sum_A))