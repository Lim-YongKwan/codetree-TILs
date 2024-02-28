a, b = map(int, input().split())

def find(a, b):
    answer = 0
    for i in range(a, b+1):
        if i % 2 != 0:
            if i % 10 != 5:
                if not (i % 3 == 0 and i % 9 != 0):
                    answer += 1
    return answer

print(find(a,b))