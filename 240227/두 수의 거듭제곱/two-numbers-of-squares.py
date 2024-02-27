def find_answer(a, b):
    answer = 1
    for i in range(1,b+1):
        answer *= a
    return answer

a, b = map(int, input().split())
print(find_answer(a,b))