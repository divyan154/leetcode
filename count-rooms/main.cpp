
#include <bits/stdc++.h>
using namespace std;
int n, m;
bool in_range(int x, int y){
    return (x >= 0 && x < n && y >= 0 && y < m);
}

void dfs(int i, int j , vector<vector<char>>&grid, vector<vector<bool>>&vis){
    vis[i][j] = 1;
    vector <int> dX = {-1 ,0, 0 , 1};
    vector <int> dY = {0, -1 , 1 , 0};
    
    for(int k = 0 ; k < 4 ; k++){
        int X = i + dX[k];
        int Y = j + dY[k];
        if(in_range(X,Y) && !vis[X][Y] && grid[X][Y] == '.')
        dfs(X,Y,grid,vis);
    }
    
}

int main()
{
//   int n, m;
  cin >> n >> m;
  vector <vector<char>>grid(n,vector<char>(m));
  for(int i = 0 ; i < n ; i++){
      for(int j = 0 ; j < m ; j++){
          cin >> grid[i][j];
      }
  }
  
vector<vector<bool>>vis(n,vector<bool>(m,0)); // visited array
int count = 0;
for(int i = 0 ; i < n ; i++){
    for(int j = 0 ; j < m ; j++){
        if(!vis[i][j] && grid[i][j] == '.')
        {
            dfs(i,j,grid,vis);
            count++;
        }
    }
}
cout << count;

    return 0;
}