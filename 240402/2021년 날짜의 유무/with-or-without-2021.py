M, D = map(int, input().split())

def is_Month(M):
    if M <= 12 and M >= 1:
        return True
    return False

def is_Day(D):
    if D <= 31 and D >= 1:
        return True
    return False

if is_Month(M) and is_Day(D):
    print("Yes")
else:
    print("No")