
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
	
	// Dikshtra Algorithm 
   
   vector <bool> vis(n+1,false);
   vector<int> dis(n+1,1e8);
   vector <int> p(n+1);
   
   priority_queue<pair<int,int>,vector<pair<int,int>>,greater<pair<int,int>>> pq; // priority_queue for min distance handling
   pq.push({0,1});
   dis[1] = 0;
   vis[1] = 1;
   
   while(!pq.empty()){
       int dist = pq.top().first;
       int u = pq.top().second;
       pq.pop();
       for(auto it : adj[u]){
           if(!vis[it] ){
              if(dist + 1 < dis[it]){
              dis[it] = dist + 1;
              vis[it] = 1;
              p[it] = u;
              pq.push({dis[it],it});
              }
               
           }
       }
       
       
   }
   
   if(dis[n] == 1e8)
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