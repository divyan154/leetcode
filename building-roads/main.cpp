
#include <bits/stdc++.h>
using namespace std;
void dfs(int node, vector<bool> &vis, vector<vector<int>> &adj) {
	vis[node] = 1;
	for(int neighboures : adj[node]) {
		if(!vis[neighboures])
			dfs(neighboures,vis,adj);
	}
}


int main()
{
	int n,m;
	cin>>n>>m;

	vector<vector<int>> adj(n+1);

	for(int i = 0 ; i < m ; i++) {
		int a,b;
		cin>>a>>b;
		adj[a].push_back(b);
		adj[b].push_back(a);
	}

	// Count total no of disconnected Components
	int cnt = 0;
	vector<bool> vis(n+1,false);
	vector<int> edge;
	for(int i = 1 ; i <= n ; i++) {
		if(!vis[i])
		{ 
		    edge.push_back(i);
			cnt++;
			dfs(i,vis,adj);
		}
	}
	cout<< cnt-1<<endl;
   for(int i = 0 ; i < edge.size() - 1 ; i++){
       cout << edge[i] << " "<<edge[i+1]<<endl;
   }
 
	
	return 0;
}