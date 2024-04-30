# 변수 선언 및 입력
n = int(input())
string = input()

# 모든 쌍을 다 잡아봅니다.
cnt = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if string[i] == 'C' and string[j] == 'O' and string[k] == 'W':
                cnt += 1

print(cnt)