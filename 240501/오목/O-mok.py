arr = []
arr2 = []
black_win = 0
white_win = 0

for i in range(19):
    arr.append(list(map(int, input().split())))

for i in range(19):
    for j in range(19):
        if arr[i][j] == 1:
            arr2.append([i, j+2, [arr[i][j], arr[i][j+1], arr[i][j+2], arr[i][j+3], arr[i][j+4]]])
            arr2.append([i+2, j, [arr[i][j], arr[i+1][j], arr[i+2][j], arr[i+3][j], arr[i+4][j]]])
            arr2.append([i+2, j+2, [arr[i][j], arr[i+1][j+1], arr[i+2][j+2], arr[i+3][j+3],arr[i+4][j+4]]])
            if i >=4 :
                arr2.append([i-2, j+2, [arr[i][j], arr[i-1][j+1], arr[i-2][j+2], arr[i-3][j+3], arr[i-4][j+4]]])
        if arr[i][j] == 2:
            arr2.append([i, j+2, [arr[i][j], arr[i][j+1], arr[i][j+2], arr[i][j+3], arr[i][j+4]]])
            arr2.append([i+2, j, [arr[i][j], arr[i+1][j], arr[i+2][j], arr[i+3][j], arr[i+4][j]]])
            arr2.append([i+2, j+2, [arr[i][j], arr[i+1][j+1], arr[i+2][j+2], arr[i+3][j+3],arr[i+4][j+4]]])
            if i >=4 :
                arr2.append([i-2, j+2, [arr[i][j], arr[i-1][j+1], arr[i-2][j+2], arr[i-3][j+3], arr[i-4][j+4]]])

for i in range(len(arr2)):
    if [1, 1, 1, 1, 1] in arr2[i]:
        black_win = 1
        print(1)
        print(arr2[i][0]+1, arr2[i][1]+1)
    if [2, 2, 2, 2, 2] in arr2[i]:
        white_win = 1
        print(2)
        print(arr2[i][0]+1, arr2[i][1]+1)

if black_win ==0 and white_win == 0:
    print(0)