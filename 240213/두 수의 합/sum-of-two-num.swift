var input = readLine()!.split(separator: " ").map { Int(String($0))!}
var arr = readLine()!.split(separator: " ").map{Int(String($0))!}

arr.sort()
var k = input[1]

var dic = [Int: Int]()
var exist = [Int: Int]()
var answer = 0

for i in stride(from: 0, to: arr.count, by: 1) {
    var temp = arr[i]
    dic[temp] = 0
}

for i in stride(from: 0, to: arr.count, by: 1) {
    var temp = arr[i]
    dic[temp]! += 1
}

for i in stride(from: 0, to: arr.count, by: 1) {
    var temp = k - arr[i]

    if(dic[temp] == 1 && dic[temp] != nil && exist[temp] == nil) {
        answer += 1
    }
    else if(dic[temp] != nil && dic[temp] != 1 && dic[temp] != 0 && exist[temp] == nil) {
        answer += dic[temp]! * (dic[temp]! - 1) / 2
    }
    exist[arr[i]] = 1
}

print(answer)