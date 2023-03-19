#include <iostream>
#include <vector>
#include <algorithm>
#include <deque>

using namespace std;

int abs(int & a){
    if(a>0) return a;
    return -a;
}


struct POST{
    int s;
    int e;
    int nums;
};

bool comp(POST &a, POST&b){
    if(a.e==b.e){
        return a.e < b.e;
    }
    return a.e < b.e;
}

vector<POST> vec;
deque<POST> deq;

int store[30001];

int main(void){
    ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);
    int n, m, t;
    cin >> n >> m;
    cin >> t;
    vec.resize(t);
    for(int i = 0;i<t;i++){
        cin >> vec[i].s >> vec[i].e >> vec[i].nums;

    }

    sort(vec.begin(), vec.end(), comp);

    int cnt = 0;
    for(int idx = 0;idx<t;idx++){
        int index = vec[idx].s;
        int tmp = 0;
        for(int j = vec[idx].s; j<vec[idx].e;j++){
            if(tmp < store[j]){
                tmp = store[j];
                index = j;
            }
        }
        tmp = (store[index] + vec[idx].nums > m) ? abs(store[index]-m) : vec[idx].nums;
        if(tmp==0) continue;
        cnt += tmp;
        for(int j = vec[idx].s; j<vec[idx].e;j++){
            store[j] += tmp;
        }
    
        // for(int i = Mi;i<=M;i++)
        //     cout << store[i] << " ";
        // cout << " " << vec[idx].nums << " " << index << '\n';
        // cout << vec[idx].s << " " << vec[idx].e << " " << vec[idx].nums << '\n';
    }
    cout << cnt << '\n';
}