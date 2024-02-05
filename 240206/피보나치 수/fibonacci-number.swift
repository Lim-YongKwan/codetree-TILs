var n = Int(readLine()!)!

var arr = Array(repeating: 0, count: 50)
arr[0] = 0
arr[1] = 1
arr[2] = 1


for i in stride(from: 3, to: n + 1, by: 1) {
    arr[i] = arr[i - 1] + arr[i - 2]
}

print(arr[n])