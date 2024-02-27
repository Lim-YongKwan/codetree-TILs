a, b = map(int, input().split())

def prime(a, b):
    add_prime_number = 0
    for i in range(a, b+1):
        for j in range(2, i+1):
            if j == i:
                add_prime_number += i
            if i % j == 0:
                break
    return add_prime_number

print(prime(a,b))