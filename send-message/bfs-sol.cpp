
#include <bits/stdc++.h>
using namespace std;

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
	
	// Bfs algorithm
   
   vector <bool> vis(n+1,false);
   vector<int> dis(n+1,0);
   vector <int> p(n+1);
   
   queue<int> q; // queue
   q.push(1);
   dis[1] = 0;
   vis[1] = 1;
   
   while(!q.empty()){
       int u = q.front();
       
       q.pop();
       for(auto v : adj[u]){
           if(!vis[v] ){
              dis[v] = dis[u] + 1;
              p[v] = u;
              vis[v] = 1;
              q.push(v);
           }
       }
       
       
   }
   
   if(!dis[n])
   cout << "IMPOSSIBLE" <<endl;
   else{
   int k = dis[n];
   cout << k + 1<<endl;
   
   //path is reversely generated through parent array
   vector<int> res(k+1);
   int u = n;
   for(int i = k ; i >= 0 ; i--){
       res[i] = u;
       u = p[u];
   }
   
   for(int i = 0 ; i < res.size() ; i++)
   cout << res[i] << " ";
   
   cout << endl;}
	return 0;
}