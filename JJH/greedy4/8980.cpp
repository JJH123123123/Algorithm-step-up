#include <iostream>
#include <algorithm>
#include <utility>
#include <queue>

using namespace std;
typedef pair<int, int> pii;

int t, n, m;

struct POST{
    int s,e,v;
}P[60001];

bool cmp(const POST & a, const POST & b){
    // if(a.e == b.e){
    //     return a.s < b.s;
    // }
    return a.e < b.e;
}

int abs(int & a){
    return (a>0) ? a : -a;
}

int budget[60001];

int main(void){
    ios::sync_with_stdio(false);cin.tie(0);
    cin >> n >> m;
    cin >> t;
    fill(budget, budget + n+1, m);
    for(int i = 0;i<t;i++){
        cin >> P[i].s >> P[i].e >> P[i].v;
        // vec.push_back(P[i]);
    }

    sort(P, P+t, cmp);
    // for(int i = 0;i<t;i++){
    //     cout << P[i].s << " " << P[i].e << '\n';
    // }
    int cnt = 0;
    for(int i = 0;i<t;i++){
        int tmp = 1000000;

        // find min
        for(int s = P[i].s; s < P[i].e;s++){
            tmp = min(budget[s], tmp);
        }

        // cout << '\n';
        // for(int i = 0;i<=5;i++){
        //     cout << budget[i] << " ";
        // }
        // cout << '\n';
        
        tmp = min(tmp, P[i].v);
        if(tmp == 0 || tmp == 1000000) continue;
        cnt += tmp;
        for(int j = P[i].s; j<P[i].e; j++){
            budget[j] -= tmp;
        }
    }
    cout << cnt << '\n';
}