#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>
using namespace std;

int n, m;
priority_queue<long long, vector<long long >, greater<long long>> pq;

int main(void){
    ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);
    cin >> n >> m;
    for(int i=0;i<n;i++){
        int tmp;
        cin >> tmp;
        pq.push(tmp);
    }

    long long cnt = 0;
    for (int i = 0;i<m;i++){
        long long first = pq.top(); pq.pop(); 
        long long second = pq.top(); pq.pop();
        long long tmp = first + second;
        pq.push(tmp); pq.push(tmp);
    }

    while(!pq.empty()){
        cnt += pq.top(); pq.pop();
    }
    cout << cnt << '\n';
}