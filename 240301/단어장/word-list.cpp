#include <iostream>
#include <vector>
#include <map>
#include <string>

using namespace std;

int main() {
    int n;
    cin>>n;
    
    map<string, int> mp;

    for(int i = 0;i<n;i++){
        string s;
        cin>>s;
        if(mp.count(s) ) {
            mp[s] += 1;
        }
        else {
            mp.insert(make_pair(s, 1));
        }
    }
    
    for(auto iter = mp.begin();iter != mp.end();iter++){
        cout<<iter->first<<" "<<iter->second<<endl;
    }

    return 0;
}