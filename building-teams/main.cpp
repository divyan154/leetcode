
#include <bits/stdc++.h>
using namespace std;
 
bool dfs(int node, vector <int> &team, int ass_team,vector<vector<int>>&adj){
    team[node] = ass_team;
    
    ass_team = (ass_team == 1) ? 2 : 1;
    
    for(auto v: adj[node]){
        if(!team[v]){
        if(!dfs(v,team,ass_team,adj))
        return false;
        }
        else if(team[v] != ass_team)
        return false;
    }
    return true;
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
	
	// dfs algorithm
   vector <int> team(n+1);
   bool ans = false;
   for(int i = 1 ; i <= n ; i++){
       if(!team[i]){
        ans = dfs(i,team,1,adj);
        if(ans == false)
        break;
           
       }
   }
   if(ans == false)
   cout << "IMPOSSIBLE"<<endl;
   else{
       
       for(int i = 1 ; i <= n ; i++)
       cout << team[i]<< " ";
       cout <<endl;
   }

	return 0;
}