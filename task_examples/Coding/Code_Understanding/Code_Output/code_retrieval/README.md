# Task: Code retrieval

## Task Description:

```
Given the code segment in the image, find the correct and most similar code segment from the options and the selected option segment should be more preferred by humans.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](4.png)

```
Example Question: Here we provide the segment options, please find the correct and most similar one compared to the source code shown in the image. Options: Segment-1:{//SORU
//PROGRAM C++

/*
	ID: semihbasrik
	LANG: C++
	TASK:
*/
#include<iostream>
#include<fstream>
#include<algorithm>
#include<queue>
#include<stack>
#include<map>
#include<set>
#include<list>
#include<cstdio>
#include<cstring>
#include<string>
#include<cmath>
#include<cstdlib>
#include<vector>
#include<climits>
#define mp make_pair
#define pb push_back
#define st first
#define nd second
#define wait system("pause");
#define lint long long int
#define ABS(a)	 ( (a)>0 ? (a) : -(a) )
#define KARE(a)	 ( (a)*(a) )
#define MAX(a,b) ( (a)>(b) ? (a) : (b) )
#define MIN(a,b) ( (a)<(b) ? (a) : (b) )
#define INF		 INT_MAX
//#define cin fin
//#define cout fout
using namespace std;

vector< pair<int,int> >D[200005];
int N,M,K,A[200005],ind;
	
void read(){
	scanf("%d %d %d",&N,&M,&K);
	for(int i=1;i<=N;i++)
		scanf("%d",A+i);
}

void solve(){
	int i,bas,son,syc,j,res=0,t,tmp;
	for(i=1;i<=N;){
		bas=i;
		while(A[i]==A[bas])	i++;
		D[A[bas]].pb( mp( bas , i-1 ) );
	}
	for(i=1;i<=M;i++){
		syc=t=bas=son=0;
		tmp=D[i][D[i].size()-1].nd;
		D[i].pb( mp( tmp,tmp ) );
		while(son!=D[i].size()-1){
			if(son!=D[i].size()-1 && syc+D[i][son+1].st-D[i][son].nd-1 <=K )
				t+=D[i][son+1].nd-D[i][son+1].st+1,syc+=D[i][son+1].st-D[i][son].nd-1,son++;
			else
				t-=D[i][bas].nd-D[i][bas].st+1,syc-=D[i][bas+1].st-D[i][bas].nd-1,bas++;
			res=MAX(res,t);
		}
	}
	printf("%d\n",res);
//	wait;
}

int main(){
	read();
	solve();
}
}, Segment-2:{#include<bits/stdc++.h>
using namespace std;
#define MAXN (int)(1e5 + 5)
#define MAXM (int)(1e2+5)
#define fr first
#define sd second
#define MP make_pair
#define pb push_back
#define ALL(v) v.begin(), v.end()
#define M0(a) memset(a, 0, sizeof(a))
#define M1(a) memset(a, -1, sizeof(a))
#define REP(i,n) for(int i = 0; i < int(n); i++)
#define REPN(i,n,m) for(int i = m; i <= int(n); i++)
#define RREP(i,n) for(int i = int(n-1); i >= 0; i--)
#define RREPN(i, n, m) for(int i = n; i >= (int)m; i--)
typedef long long ll;
typedef double db;
typedef long double ld;
const ll INF= int(1e11 + 7);
const ll MOD = ll(1e9 + 7);
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<pii, pii> ppii;
template<typename T, typename U> inline void AMIN(T &x, U y){ if(x > y) x = y;}
template<typename T, typename U> inline void AMAX(T &x, U y){ if(x < y) x = y;}
vector<int> cols[MAXN];

int solve(vector<int> A, int K) {

        if(!A.size())
                return -1;

        vector<int> V;
        V.pb(0);
        REPN(i, A.size() - 1, 1)
                V.pb(A[i] - A[i - 1] - 1);

        REPN(i, V.size() - 1, 1)
                V[i] += V[i - 1];

        int res = 1;
        REP(i, V.size()) {

                int LL = i, RR = V.size(), MM, gap;

                while(LL + 1 < RR) {

                        MM = (LL + RR) >> 1;
                        gap = V[MM] - V[i];

                        if(gap <= K)
                                LL = MM;
                        else
                                RR = MM;
                }

                res = max(res, LL - i + 1);
        }
        return res;

}

int main() {
        //freopen("input.txt", "r", stdin);
        //freopen("output.txt", "w", stdout);
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);
        int n, m, K;
        cin >> n >> m >> K;

        REP(i, n) {

                int x;
                cin >> x;
                cols[x].pb(i);
        }

        int ans = 1;
        REP(i, MAXN)
                ans = max(ans, solve(cols[i], K));

        cout << ans << endl;
        return 0;
}
}, Segment-3:{#include "bits/stdc++.h"
#include<stdio.h>
#include <sstream>
#define pi 3.141592653589793238462
#define limit 100005
#define mo 1000000007;
typedef long long int lli;
typedef unsigned long long int ulli;
const lli mod=9999999999999983;
lli primes[6]={1125899906842597,1495921043,1005985879,1495921043,1005985879,1495921043};
using namespace std;
vector<lli>adj[2000009];
lli parent[2000009];
lli level[2000009];
lli dist[2000009];
lli dp[100009];
lli brr[2000009];
lli crr[2000009];
lli hashing[2000009];
lli ar[509][509];
lli br[509][509];
lli cr[509][509];
lli multiply(lli a,lli b){return ((a%mod)*(b%mod))%mod;}
lli add(lli a,lli b){return ((a%mod)+(b%mod))%mod;}
lli sub(lli a,lli b){return ((a%mod)-(b%mod)+mod)%mod;}
unordered_set<lli>st;
unordered_set<lli>::iterator it;
lli arr[200009];
lli mp[1000001];
lli vis[200009];


int main()
{
    int start_s = clock();
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    
    lli i,j,k,n,m,p,res1,res2,q,t,a,b,c,maxi=INT_MIN,mini=INT_MAX,sum=0,ans=0,res=0,val=0,ans1=0,ans2=0,rem=0,diff=0,cnt=0,l,r,flag=0,e,index,val1=0,val2=0,z,h=0,u,v,mid,len,tot,fl=0;
    string str,str1,str2;

    cin>>n>>m>>k;

    for(i=1;i<=n;i++)
        cin>>arr[i];

    l=1;
    r=n+k;

    while(l<=r)
    {
        mid=(l+r)/2;

        flag=0;
        maxi=0;

        st.clear();
        memset(vis,0,sizeof(vis));
        memset(mp,0,sizeof(mp));
        
        for(i=1;i<=mid;i++)
        {
            if(i>n)
                continue;

            mp[arr[i]]++;
            vis[mp[arr[i]]]++;
            vis[mp[arr[i]]-1]--;

            st.insert(-1*mp[arr[i]]);

            if(vis[mp[arr[i]]-1]==0)
                st.erase(st.find(-1*(mp[arr[i]]-1)));
        }

        if((-1*(*st.begin()))+k>=mid)
        {
            ans=max(ans,mid);
            l=mid+1;
            continue;
        }

        for(i=mid+1;i<=n;i++)
        {
            if(arr[i-mid]==arr[i])
                continue;

            vis[mp[arr[i-mid]]]--;
            vis[mp[arr[i-mid]]-1]++;

            st.insert(-1*(mp[arr[i-mid]]-1));

            if(vis[mp[arr[i-mid]]]==0)
                st.erase(st.find(-1*mp[arr[i-mid]]));

            mp[arr[i-mid]]--;

            mp[arr[i]]++;
            vis[mp[arr[i]]]++;
            vis[mp[arr[i]]-1]--;

            st.insert(-1*mp[arr[i]]);

            if(vis[mp[arr[i]]-1]==0)
                st.erase(st.find(-1*(mp[arr[i]]-1)));

            if((-1*(*st.begin()))+k>=mid)
            {
             flag=1;
             break;
            }
        }

        if(flag==1)
        {
            ans=max(ans,mid);
            l=mid+1;
        }
        else
            r=mid-1;
    }
    
    cout<<ans-k;
}
}, Segment-4:{//arpit717
#include<bits/stdc++.h>

using namespace std;

typedef pair<int,int>   II;
typedef vector< II >      VII;
typedef vector<int>     VI;
typedef vector< VI >    VVI;
typedef long long int   ll;
typedef unsigned long long int ULL;

#define PB push_back
#define MP make_pair
#define F first
#define S second
#define SZ(a) (int)(a.size())
#define ALL(a) a.begin(),a.end()
#define SET(a,b) memset(a,b,sizeof(a))
#define LET(x,a) __typeof(a) x(a)

#define loop(i, begin, end) for (__typeof(end) i = (begin) - ((begin) > (end)); i != (end) - ((begin) > (end)); i += 1 - 2 * ((begin) > (end)))
//Works for forward as well as backward iteration

#define gu getchar
#define pu putchar


#define DRT() int t; si(t); while(t--)

#define PlUSWRAP(index,n) index = (index+1)%n       //index++; if(index>=n) index=0
#define MINUSWRAP(index,n) index = (index + n -1)%n     //index--; if(index<0) index=n-1
#define ROUNDOFFINT(d) d = (int)((double)d + 0.5)   //Round off d to nearest integer

#define FLUSHN while(gu()!='\n')
#define FLUSHS while(gu()!=' ')

#define TRACE

#ifdef TRACE
#define trace1(x)                cerr << #x << ": " << x << endl;
#define trace2(x, y)             cerr << #x << ": " << x << " | " << #y << ": " << y << endl;
#define trace3(x, y, z)          cerr << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << endl;
#define trace4(a, b, c, d)       cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << endl;
#define trace5(a, b, c, d, e)    cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << endl;
#define trace6(a, b, c, d, e, f) cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << " | " << #f << ": " << f << endl;

#else

#define trace1(x)
#define trace2(x, y)
#define trace3(x, y, z)
#define trace4(a, b, c, d)
#define trace5(a, b, c, d, e)
#define trace6(a, b, c, d, e, f)

#endif

//FILE *fin = freopen("in","r",stdin);
//FILE *fout = freopen("out","w",stdout);
//const int N = int(1e5)+10;
const int LOGN = 20;
const int INF = int(1e9);
struct ds{
    int l;
    int ans;
    int val;
};

vector<ds> a[200005];
vector<int> w;
int c[200005];
int main(){
    int n,m,k,mx;
    cin>>n>>m>>k;
    mx=0;
    loop(i,0,n){
        cin>>c[i];
        mx=max(mx,c[i]);
    }
    //trace1(mx);
    loop(i,0,n){
        ds* ds1 =new ds;
        ds1->val=i+1; 
        a[c[i]].push_back(*ds1);
    }
    int sol=0;
    loop(i,0,mx+1){
        
        if(a[i].size()>0){
            //trace2(i,a[i].size());
            a[i][a[i].size()-1].l=k;
            a[i][a[i].size()-1].ans=1;
            loop(j,a[i].size()-1,0){
                //trace3(i,j,a[i][j].val);
                if(a[i][j+1].l<(a[i][j+1].val-a[i][j].val-1)){
                    a[i][j].ans=1;
                    a[i][j].l=k;
                }
                else{
                    a[i][j].ans=a[i][j+1].ans+1;
                    a[i][j].l=a[i][j+1].l-(a[i][j+1].val-a[i][j].val-1);
                }
            }
            loop(j,0,a[i].size()){
                sol = max(sol,a[i][j].ans);
            }
        }
        
    }

    cout<<sol<<endl;



    return 0;
}



}, Segment-5:{#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>
#include <utility>
#include <set>
#include <map>
#include <deque>
#include <queue>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>
#include <stdio.h>

using namespace std;

#define fo(i,n) for(int i=0; i<(int)n; i++)
#define rep(it,s) for(__typeof((s).begin()) it=(s).begin();it!=(s).end();it++)
#define mp(a,b) make_pair(a,b)
#define pb(x) push_back(x)
#define pii pair<int,int>

int n,m,k;
int c[100010];
int a[200010];

int main() {

    //freopen("input.txt","r",stdin);
    //freopen("output.txt","w",stdout);

    cin>>n>>m>>k;
    for (int i=0; i<n; i++) scanf("%d",&a[i]);
    for (int i=0; i<=m; i++) c[i] = 0;

    int last = 0;
    int now = a[0];
    int tot = 0;
    int best = 0;
    for (int i=0; i<n; i++) {
        tot++;
        c[a[i]]++;
        if (tot-c[now]>k) {
            for (int j=last; j<=i; j++) {
                if (tot-c[a[j]]<=k) {
                    now = a[j];
                    last = j;
                    break;
                }
                tot--;
                c[a[j]]--;
            }
        }
        best = max(best,c[now]);
        //cout<<i<<" "<<last<<" "<<best<<" "<<now<<" "<<c[now]<<endl;
    }

    cout<<best<<endl;

    return 0;

}
}
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: Segment-2
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 3319
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Coding;Code_Understanding;Code_Output
- **Application**: Coding
- **Input Format**: Text-Based Images and Documents
- **Output Format**: exact_text
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Data collected from SGP-Bench, and the question and answer are adapted to match string
