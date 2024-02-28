a, b = map(int, input().split())

def find_decimal(a, b):
    answer = 0
    for i in range(a, b+1):
        for j in range(2, i+1):
            if i % j == 0:
                if j == i and find_even_number(i):
                    answer += 1
                else:
                    break
    return answer
                    
def find_even_number(n):
    num = 0
    while n > 0:
        num += n % 10
        n = n//10
    if num % 2 == 0:
        return True
    return False
        
print(find_decimal(a, b))