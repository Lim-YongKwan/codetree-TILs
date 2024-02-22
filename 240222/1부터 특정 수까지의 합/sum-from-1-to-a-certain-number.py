n = int(input())

def sum(n):
    m = 0
    for i in range(1,n+1):
        m += i
    return m//10

result = sum(n)
print(result)