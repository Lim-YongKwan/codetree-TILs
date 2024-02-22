a, b, c = map(int, input().split())

def find_min(a, b, c):
    min = 0
    if a < b:
        min = a
    else:
        min = b
    if c < min:
        min = c
    return min

print(find_min(a, b, c))