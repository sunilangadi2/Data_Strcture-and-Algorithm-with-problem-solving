#include <bits/stdc++.h>
using namespace std;

#define F first
#define S second
#define FOR(i,a,b) for (auto i = (a); i <= (b); ++i)
#define NFOR(i,a,b) for(auto i = (a); i >= (b); --i)
#define all(x) (x).begin(), (x).end()
#define sz(x) int(x.size())
typedef long long ll; typedef pair <int, int> ii; typedef vector <int> vi; const int inf = 1e9 + 7;
#define pr(...) dbs(#__VA_ARGS__, __VA_ARGS__)
template <class T> void dbs(string str, T t) {cout << str << " : " << t << endl;}
template <class T, class... S> void dbs(string str, T t, S... s) {int idx = str.find(','); cout << str.substr(0, idx) << " : " << t << ","; dbs(str.substr(idx + 1), s...);}
template <class S, class T>ostream& operator <<(ostream& os, const pair<S, T>& p) {return os << "(" << p.first << ", " << p.second << ")";}
template <class T>ostream& operator <<(ostream& os, const vector<T>& p) {os << "[ "; for (auto& it : p) os << it << " "; return os << "]";}
template <class T>ostream& operator <<(ostream& os, const set<T>& p) {os << "[ "; for (auto& it : p) os << it << " "; return os << "]";}
template <class S, class T>ostream& operator <<(ostream& os, const map<S, T>& p) {os << "[ "; for (auto& it : p) os << it << " "; return os << "]";}
template <class T> void prc(T a, T b) {cout << "["; for (T i = a; i != b; ++i) {if (i != a) cout << ", "; cout << *i;} cout << "]";cout<<endl;}

int main()
{
	ios::sync_with_stdio(0); cin.tie(0);

	int tc = 1;
	int t; cin >> t; while (t--) {
		cout << "Case #" << tc << ": ";
		++tc;
		string s; cin >> s;
		int n = sz(s);
		int pos = -1;
		FOR (i, 0, n - 1) {
			if ((s[i] - '0') % 2 == 1) {
				pos = i;
				break;
			}
		}
		if (pos == -1) {
			cout << "0\n";
		} else {
			ll ans = 1e18;
			if (s[pos] != '9') {
				string t = s;
				t[pos]++;
				FOR (it, pos+1, n - 1) t[it] = '0';
				ans = min(ans, stoll(t) - stoll(s));
			}
			string t = s;
			t[pos]--;
			FOR (it, pos + 1, n - 1) t[it] = '8';
			ans = min(ans, stoll(s) - stoll(t));
			cout << ans << "\n";
		}
	}

	return 0;
}
