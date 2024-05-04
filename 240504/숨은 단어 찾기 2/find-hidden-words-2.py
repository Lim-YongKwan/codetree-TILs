n, m = map(int, input().split())
arr = [
        list(input())
        for _ in range(n)
    ]
answer = 0

def isInborder(x, y):
    if(x >= 0 and x < m and y >= 0 and y < n):
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
            return False
        if (isInborder(nx2,ny2) == False):
            return False        
        else:
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