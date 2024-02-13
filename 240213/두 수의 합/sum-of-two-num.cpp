#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

unordered_map<long long, int> count;
int main() {
    int n,k;
    cin>>n>>k;
    vector<int> arr(n,0);

    for(int i = 0;i<n;i++){
        cin>>arr[i];
    }

    int ans = 0;
    
    for(int i = 0;i<n;i++){
        long long diff = (long long)k - arr[i];
        ans += count[diff];
        count[arr[i]]++;
    }
    cout<<ans;
    return 0;
}