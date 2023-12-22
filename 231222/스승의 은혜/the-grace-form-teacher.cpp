#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(pair<int,int> a, pair<int,int> b) {
    if((a.first + a.second) == (b.first + b.second)){
        return a.first < b.first;
    }
    return (a.first + a.second) < (b.first + b.second);
}

int main() {
    int answer = 0;
    int n,b;
    cin>>n>>b;

    vector<pair<int,int> > student(n);

    for(int i = 0;i<n;i++){
        cin>>student[i].first>>student[i].second;
    }

    sort(student.begin(),student.end(),compare);

    // for(int i = 0;i<student.size();i++){
    //     cout<<student[i].first<<" "<<student[i].second<<endl;
    // }
    //합이 작은것부터 sort가 되어야 한다.

    for(int i = 0;i<student.size();i++){
        student[i].first /= 2;
        int total = 0;
        int start = 0;
        while(start < n && total <= b) {
            total += student[start].first + student[start].second;
            start++;
        }
        answer = max(answer, start - 1);

        student[i].first *= 2;
    }

    cout<<answer<<endl;

    return 0;
}