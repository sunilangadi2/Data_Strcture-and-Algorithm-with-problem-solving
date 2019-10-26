import java.util.*;
public class Solution {
	public static void main (String [] arg) {
		Scanner sc = new Scanner(System.in);
		int T = Integer.parseInt(sc.nextLine());
		for (int ii = 1; ii<=T; ++ii) {
			int R = sc.nextInt();
			int C = sc.nextInt();
			int	H = sc.nextInt();
			int V = sc.nextInt();
			char [][] c = new char[R][];
			int chips = 0;
			for (int i = 0; i<R; ++i) {
				c[i] = sc.next().toCharArray();
				for (int j = 0; j<c[i].length; ++j)
					if (c[i][j] == '@') chips++;
			}
			int pieces = (H+1)*(V+1);
			String ans = "POSSIBLE";
			if (chips == 0) {
				System.out.printf("Case #%d: POSSIBLE\n",ii);
				continue;
			}
			if (chips % pieces != 0 || chips % (V+1) != 0 || chips % (H+1) != 0) {
				System.out.printf("Case #%d: IMPOSSIBLE\n",ii);
				continue;
			}
			int factor = chips / pieces;
			Vector<Integer> vafter = new Vector<Integer>();
			Vector<Integer> hafter = new Vector<Integer>();
			
			
			int Vtot = chips / (V+1);
			int Htot = chips / (H+1);
			
			int chipcount = 0;
			for (int j = 0; j<C; ++j) {
				for (int i = 0; i<R && vafter.size() < V; ++i) 
					if (c[i][j] == '@') chipcount++;
				if (chipcount < Vtot) {
					continue;
				} else if (chipcount == Vtot) {
					vafter.add(j);
					chipcount = 0;
				} else {
					ans = "IMPOSSIBLE";
				}
			}
			chipcount = 0;
			for (int i = 0; i<R; ++i) {
				for (int j = 0; j<C && hafter.size() < H; ++j)
					if (c[i][j] == '@') chipcount++;
				if (chipcount < Htot) {
					continue;
				} else if (chipcount == Htot) {
					hafter.add(i);
					chipcount = 0;
				} else {
					ans = "IMPOSSIBLE";
				}
			}
			if (hafter.size() != H) ans = "IMPOSSIBLE";
			if (vafter.size() != V) ans = "IMPOSSIBLE";
			
			//Final check.
			for (int i = -1; i<hafter.size() && !ans.equals("IMPOSSIBLE"); ++i) {
				int previ = (i == -1) ? -1 : hafter.get(i);
				int nexti = (i == hafter.size() - 1) ? R-1 : hafter.get(i+1);
				for (int j = -1; j<vafter.size(); ++j) {
					int prevj = (j == -1) ? -1 : vafter.get(j);
					int nextj = (j == vafter.size() - 1) ? C-1 : vafter.get(j+1);	
					int count = 0;
					for (int i1 = previ+1; i1 <= nexti; ++i1) 
						for (int j1 = prevj+1; j1<=nextj; ++j1) 
							if (c[i1][j1] == '@') count++;
							
					if (count != factor) {
						//System.err.println("Found anomaly " + count + " between row " + (previ+1) + " - " + nexti + " and column " + (prevj+1) + " - " + nextj );
						ans = "IMPOSSIBLE";
						break;
					}
				}
			}
			//System.err.println("V: " + vafter.toString());
			//System.err.println("V: " + hafter.toString());
			
			
			System.out.printf("Case #%d: %s\n",ii,ans);
		}
	}
}