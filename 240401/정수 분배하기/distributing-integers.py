n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

def is_possible(k):
    count = 0
    for elem in arr:
        count += int(elem/k)
    if count >= m:
        return True
    return False

left = 1
right = max(arr)
answer = 0
while left <= right:
    mid = (left + right)//2
    if is_possible(mid):
        left = mid + 1
        answer = max(answer, mid)
    else:
        right = mid - 1
print(answer)