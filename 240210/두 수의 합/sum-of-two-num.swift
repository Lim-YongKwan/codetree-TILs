var input = readLine()!.split(separator: " ").map{Int(String($0))!}
var nums = readLine()!.split(separator: " ").map{ Int(String($0))!}

var k = input[1]
nums.sort()

var dict = [Int: Int]()

for i in stride(from: 0, to: nums.count, by: 1) {
    dict[nums[i]] = 1
}

var answer = 0

for i in stride(from: 0, to: nums.count, by: 1) {
    var temp = k - nums[i];
    if(dict[temp] == 1) {
        answer += 1
    }
}

print(answer / 2)