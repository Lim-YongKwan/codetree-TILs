n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

def find_min_idx(target):
    min_idx = n
    left, right = 0, n-1
    while left <= right:
        mid = (left + right)//2
        if arr[mid] >= target:
            min_idx = min(min_idx, mid)
            right = mid -1
        else:
            left = mid + 1
    return min_idx

for i in range(m):
    answer = find_min_idx(arr2[i])
    if answer < n and arr[answer] == arr2[i]:
        print(answer+1)
    else:
        print(-1)