#include <bits/stdc++.h>
using namespace std;

#define mp make_pair
#define pb push_back
#define MOD 1000000007LL
#define INF 1000000000000000018LL
#define F first
#define S second
#define ll long long
#define ld long double
#define eps 1e-9

ll gcd(ll a, ll b)
{
    if(a == 0LL)
        return b;
    if(b == 0LL)
        return a;
    return gcd(b, a%b);
}

typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

const int N = 100005;
const int LOGN = 17;
int tab[LOGN][N];
int C[N], D[N], L[N], R[N];

void pre(int n)
{
    for(int i = 1; i<=n; i++)
        tab[0][i] = D[i];
    for(int j = 1; (1<<j) <= n; j++)
        for(int i = 1; i + (1<<j) - 1 <= n; i++)
            tab[j][i] = max(tab[j-1][i], tab[j-1][i + (1<<(j-1))]);

    stack<int> s;
    while(!s.empty())
        s.pop();
    for(int i = 1; i<=n; i++)
    {
        while(!s.empty() && C[s.top()] <= C[i])
        {
            R[s.top()] = i-1;
            s.pop();
        }
        if(s.empty())
            L[i] = 1;
        else
            L[i] = s.top() + 1;
        s.push(i);
    }
    while(!s.empty())
    {
        R[s.top()] = n;
        s.pop();
    }

    return;
}

int query(int l, int r)
{
    int x = log2(r - l + 1);
    return max(tab[x][l], tab[x][r - (1<<x) + 1]);
}

void solve()
{
    int n, k;
    cin >> n >> k;
    for(int i = 1; i<=n; i++)
        cin >> C[i];
    for(int i = 1; i<=n; i++)
        cin >> D[i];
    pre(n);
    // for(int i = 1; i<=n; i++)
        // cout << L[i] << " " << R[i] << "\n";
    // cout << "\n";
    ll ans = 0LL;
    for(int i = 1; i<=n; i++)
    {
        if(i - L[i] < R[i] - i)
        {
            for(int j = L[i]; j<=i; j++)
            {
                int lw, hi;

                int l = j, r = n, mid;
                while(l < r)
                {
                    mid = ((l+r)>>1) + 1;
                    if(query(j, mid) > C[i] + k)
                        r = mid - 1;
                    else
                        l = mid;
                }
                assert(l == r);
                if(query(j, l) > C[i] + k)
                    l--;
                hi = l;

                l = j;
                r = n;
                while(l < r)
                {
                    mid = (l+r)>>1;
                    if(query(j, mid) < C[i] - k)
                        l = mid + 1;
                    else
                        r = mid;
                }
                assert(l == r);
                if(query(j, l) < C[i] - k)
                    l++;

                lw = l;

                // cout << i << " " << lw << " " << hi << "\n";

                lw = max(lw, i);
                hi = min(hi, R[i]);

                ans = ans + 1LL*max(0, hi - lw + 1);
            }
        }
        else
        {
            for(int j = i; j<=R[i]; j++)
            {
                int lw, hi;

                int l = 1, r = j, mid;
                while(l < r)
                {
                    mid = (l+r)>>1;
                    if(query(mid, j) > C[i] + k)
                        l = mid + 1;
                    else
                        r = mid;
                }
                assert(l == r);
                if(query(l, j) > C[i] + k)
                    l++;
                lw = l;

                l = 1;
                r = j;
                while(l < r)
                {
                    mid = ((l+r)>>1) + 1;
                    if(query(mid, j) < C[i] - k)
                        r = mid - 1;
                    else
                        l = mid;
                }
                assert(l == r);
                if(query(l, j) < C[i] - k)
                    l--;

                hi = l;

                lw = max(lw, L[i]);
                hi = min(hi, i);

                ans = ans + 1LL*max(0, hi - lw + 1);
            }
        }
    }
    cout << ans << "\n";

    return;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    
    // freopen("in.in", "r", stdin);
    // freopen("out.out", "w", stdout);

    clock_t clk = clock();
    
    int t = 1;
    cin >> t;
    for(int tests = 1; tests <= t; tests++)
    {
        cout << "Case #" << tests << ": ";
        solve();
    }

    clk = clock() - clk;
    cerr << "Time Elapsed: " << fixed << setprecision(10) << ((long double)clk)/CLOCKS_PER_SEC << "\n";

    return 0;
}