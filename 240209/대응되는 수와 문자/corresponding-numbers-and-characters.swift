var n = readLine()!.split(separator: " ").map { Int(String($0))! }

var dic = [String: Int]()
var arr = Array(repeating: "", count: n[0] + 5)

for i in stride(from: 0, to: Int(n[0]), by: 1){
    var temp = readLine()!
    dic[String(temp)] = i + 1
    arr[i] = String(temp)
}

for i in stride(from: 0, to: Int(n[1]), by: 1){
    var temp = readLine()!
    if (temp.allSatisfy({$0.isNumber})) {
        print(arr[Int(temp)! - 1])
    }
    else {
        print(dic[String(temp)]!)
    }
}