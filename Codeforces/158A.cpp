#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <queue>
#include <deque>
#include <bitset>
#include <iterator>
#include <list>
#include <stack>
#include <map>
#include <set>
#include <functional>
#include <numeric>
#include <utility>
#include <limits>
#include <time.h>
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>

using namespace std;

#define ar array
#define ll long long

const int MAX_N = 1e5 + 1;
const int MOD = 1e9 + 7;
const int INF = 1e9;
const ll LINF = 1e18;



int main() {
    int n,s,k,m,res=0;
    cin>>n>>s;
    for (int i =1;i<=n;i++){
        cin>>k;
        if (i<=s && k>0){
            m=k;
            res++;
        }else if(k==m && k>0){
            res++;
        }
    }
    cout<<res;
    return 0;
}