#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n,m;
    cin>>n>>m;
    vector<int> num(n + 1, 0);
    for(int i = 0;i<=n;i++){
        cin>>num[i];
    }
    vector<int> pre_fix(n + 1 ,0);
    for(int i = 0;i<=n;i++){
        pre_fix[i] = num[i] + pre_fix[i - 1];
    }

    int answer = -100000;
    for(int i = m - 1;i<=n;i++){
        answer = max(answer, pre_fix[i] - pre_fix[i - m + 1]);
    }
    cout<<answer<<endl;
    return 0;
}