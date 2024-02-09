var n = Int(readLine()!)!
var arr = Array(repeating: 0, count: n + 5)
arr[0] = 0
arr[1] = 1
arr[2] = 2
arr[3] = 3
arr[4] = 5
//중복 제거 필요.

for i in stride(from: 5, to: n + 1, by: 1){
    arr[i] = arr[i - 1] + arr[i - 2]
}

print(arr[n])