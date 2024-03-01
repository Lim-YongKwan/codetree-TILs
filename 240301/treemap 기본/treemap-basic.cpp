#include <iostream>
#include <map>
#include <algorithm>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

map<int ,int> mp;

vector<string> splited(string s){
    istringstream iss(s);
    vector<string> answer;
    string buffer;    
    char delimeter = ' ';

    while(getline(iss, buffer, delimeter)){
        answer.push_back(buffer);    
    }
    return answer;    
}

int main() {
    int testcase = 0;
    cin>>testcase;

    for(int T = 0; T<=testcase;T++) {
        string str;        
        getline(cin, str);
        if(T == 0 ) continue;
        vector<string> result;
        result = splited(str);

        if(result[0] == "add") {
            int a = stoi(result[1]);
            int b = stoi(result[2]);
            mp[a] = b;
        }
        else if(result[0] == "find") {
            int a = stoi(result[1]);
            if(mp[a])
                cout<<mp[a]<<endl;
            else{
                cout<<"None"<<endl;
            }
        }
        else if(result[0] == "remove") {
            int a = stoi(result[1]);
            mp.erase(a);
        }
        else if(result[0] == "print_list") {
            if(mp.size() == 0){
                cout<<"None"<<endl;
                continue;
            }
            bool flag = false;
            for(auto iter = mp.begin(); iter != mp.end();iter++) {
                if(iter->second == 0) continue;
                else if(iter->second) flag = true;
                cout<<iter->second<<" ";
            }
            if(flag == false) cout<<"None"<<endl;
            cout<<endl;
        }
    }
    return 0;
}