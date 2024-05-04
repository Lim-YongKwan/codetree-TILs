n, m = map(int, input().split())
arr = [
        list(input())
        for _ in range(n)
    ]
answer = 0

def isInborder(x, y):
    if(x >= 0 and x < n and y >= 0 and y < m):
        return True
    return False

def is_LEE_True(x, y):
    global answer
    dx = [1, 1, 1, 0, 0, -1, -1, -1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        nx2 = nx + dx[i]
        ny2 = ny + dy[i]
        if (isInborder(nx,ny) == False):
            continue
        if (isInborder(nx2,ny2) == False):
            continue
        else:
            if arr[nx][ny] == "E" and arr[nx2][ny2] == "E":
                #print(x,y, nx, ny, nx2, ny2)
                answer += 1
    return answer
        

def isLEE():
    # 범위 안에 있는지 확인하는 함수
    # true라면 그대로 진행
    global answer
    for i in range(n):
        for j in range(m):
        # 1,1 => n, m까지 진행.
            if arr[i][j] == 'L':
                is_LEE_True(i, j)
    print(answer)

isLEE()