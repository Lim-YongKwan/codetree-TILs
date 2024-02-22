n, m = map(int, input().split())

def find_lcm(a, b):
    for i in range(1, a*b):
        lcm = 0
        if i % a == 0 and i % b == 0:
            print(i)
            break


find_lcm(n, m)