n = int(input())
arr = []
arr2 = []
global answer
answer = -1
sum_val = 0
isVisited = [0 for _ in range(n)]

for _ in range(n):
    arr.append(int(input()))

def backTracking(cnt):
    if cnt == 3:
        str_1 = str(arr2[0])
        str_2 = str(arr2[1])
        str_3 = str(arr2[2])

        maxNum = max(arr2[0], arr2[1])
        maxNum = max(maxNum, arr2[2])
        max_len = len(str(maxNum))

#        print(str_1,str_2,str_3)
        
        # reverse로 모두 뒤집기
        str_1 = str_1[::-1]
        str_2 = str_2[::-1]
        str_3 = str_3[::-1]         

        for i in range(len(str_1),max_len):
            str_1 += '0'
        for i in range(len(str_2),max_len):
            str_2 += '0'
        for i in range(len(str_3),max_len):
            str_3 += '0'

        for i in range(max_len):
            if (int(str_1[i]) + int(str_2[i]) + int(str_3[i])) >= 10:
                return

        global answer;
        answer = max(answer, arr2[0] + arr2[1] + arr2[2])        
        return
    for i in range(n):
        if isVisited[i] == 0:
            isVisited[i] = 1
            arr2.append(arr[i])
            backTracking(cnt + 1)            
            arr2.pop()
            isVisited[i] = 0

backTracking(0)

# for i in range(n):
#     for j in range(i+1,n):
#         for k in range(j+1,n):
#             print(arr[i],arr[j],arr[k])
#             sum_val = arr[i] + arr[j] + arr[k]
#             answer = max(answer, sum_val)

# if sum_val == 0:
#     print(-1)
# else:
#     print(answer)

print(answer)