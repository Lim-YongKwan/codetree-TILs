def is_year(n):
    if n % 4 == 0:
        return True
    if n % 100 == 0 and n % 400 != 0:
        return False
    return False

n = int(input())
if is_year(n) == True:
    print("true")
else:
    print("false")