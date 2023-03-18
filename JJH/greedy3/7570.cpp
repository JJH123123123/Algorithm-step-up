#include <iostream>
using namespace std;

int LIS[1000001];
int main(void){
    ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);
    int n;
    
    cin >> n;
    int tmp;
    int ans = -1;
    for (int i = 0;i<n;i++){
        cin >> tmp;
        LIS[tmp] = LIS[tmp-1] + 1;
        ans = max(LIS[tmp], ans);
    }
    cout << n - ans  << '\n';
}

