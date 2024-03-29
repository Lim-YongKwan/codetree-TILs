#include <iostream>
#include <map>
#include <string>
#include <cmath>

using namespace std;

int main() {
    int T;
    cin>>T;
    map<string ,double> mp;
    double total = 0;
    for(int testcase = 0; testcase < T; testcase++) {
        string s;
        cin>>s;
        mp[s] += 1;        
        total++;
    }
    cout<<fixed;
    cout.precision(4);

    for(auto iter = mp.begin(); iter != mp.end(); iter++) {
        cout<<iter->first<<" "<< (round)(iter->second * 1000000 / total) / 10000<<endl;
    }
    
    return 0;
}