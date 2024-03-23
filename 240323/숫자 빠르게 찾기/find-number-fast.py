n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr2 = [0] * m

def find_idx(target):
    idx = -1
    left, right = 0, n-1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            idx = mid
            break
        if arr[mid] > target:
            right = mid-1
        else:
            left = mid+1
    if idx != -1:
        idx += 1
    return idx

for i in range(m):
    arr2[i] = int(input())
    print(find_idx(arr2[i]))