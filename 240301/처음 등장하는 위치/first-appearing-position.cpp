#include <iostream>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

int main() {
    int n;
    cin>>n;
    vector<int> vec(n + 1,0);
    map<int, int> mp;

    for(int i = 1;i<=n;i++){
        cin>>vec[i];
        if(mp[vec[i]] == 0)
            mp[vec[i]] = i;
    }

    for(auto iter = mp.begin(); iter != mp.end();iter++) {
        cout<<iter->first<<" "<<iter->second<<endl;
    }

    return 0;
}