var n = Int(readLine()!)!
var arr = Array(repeating: 0, count: n + 4)
arr[0] = 0
arr[1] = 0
arr[2] = 1
arr[3] = 1

for i in stride(from:4, to:n + 1, by:1){
    arr[i] = (arr[i - 3] + arr[i - 2]) % 10007
}

print(arr[n])