def is_3x_number(a, b):
    answer = 0
    for i in range(a,b+1):
        if i % 3 == 0 or is_3_number(i):
            answer += 1
    return answer

def is_3_number(n):
    while n > 0 :
        if n % 10 == 3 or n % 10 == 6 or n % 10 == 9:
            return True
        n = n//10

a, b = map(int, input().split())
print(is_3x_number(a, b))