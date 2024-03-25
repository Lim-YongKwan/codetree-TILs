n, m = map(int, input().split())
arr_n = list(map(int, input().split()))

def find_point(m1, m2):
    count = 0
    for arr in arr_n :
        if arr >= m1 and arr <= m2:
            count += 1
    return count

for i in range(m):
    m1, m2 = map(int, input().split())
    print(find_point(m1, m2))