class Solution {
    
public:
    bool canFinish(int n, vector<vector<int>>& prerequisites) {
        
        vector<vector<int>> adjList(n);

        for(int i = 0 ; i < prerequisites.size(); i++){
            int u = prerequisites[i][0];
            int v = prerequisites[i][1];
            adjList[v].push_back(u);
        }

        vector <int> indegree(n,0);
        vector <int> ans;
        for(int i = 0 ; i < n ; i++){
            for(auto it : adjList[i])
            indegree[it]++;
        }

        queue<int> q;
        for(int i = 0 ; i < n ; i++){
            if(indegree[i] == 0)
            q.push(i);
        }

        while(!q.empty()){
            int node = q.front();q.pop();
            ans.push_back(node);
            for(auto it: adjList[node]){
                indegree[it]--;
                if(indegree[it] == 0)
                q.push(it);
            }
        }
        if(ans.size() == n)
        return true;
        return false;
    }
};