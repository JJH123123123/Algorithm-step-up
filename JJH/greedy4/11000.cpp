#include <iostream>
#include <queue>
#include <utility>
#include <algorithm>

using namespace std;
typedef pair<int, int> pii;
vector<pii> schedule;
priority_queue<int, vector<int>, greater<int>> pq;

bool cmp(const pii &a, const pii &b){
    if(a.first == b.first){
        return a.second < b.second;
    }
    return a.first < b.first;
}

int main(void){
    ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);
    int n;
    cin >> n;
    for (int i=0;i<n;i++){
        int s,e;
        cin >> s >> e;
        schedule.push_back({s,e});
    }
    sort(schedule.begin(), schedule.end(), cmp);
    pq.push(schedule[0].second);
    for (int  i = 1; i < n; i++)
    {
        /* code */
        if(pq.top() <= schedule[i].first){
            pq.pop();
            pq.push(schedule[i].second);
        }else{
            pq.push(schedule[i].second);
        }
    }
    cout << pq.size() << '\n';
}