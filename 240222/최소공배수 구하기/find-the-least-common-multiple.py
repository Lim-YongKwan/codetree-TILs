n, m = map(int, input().split())

def find_lcm(a, b):
    for i in range(max(a,b), (a*b)+1):
        lcm = 0
        if i % a == 0 and i % b == 0:
            print(i)
            break

find_lcm(n, m)