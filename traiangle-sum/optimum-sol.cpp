class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        int n = triangle.size();
        //dp[j] -> represents min sum of from i,j to the end in triangle 
        vector <int> dp(triangle.back());
  
        for(int layer = n- 2 ; layer >= 0 ; layer--){
            for(int j = 0 ; j <= layer ; j++){
                dp[j] = min(dp[j],dp[j+1]) + triangle[layer][j];
            }
        }
        return dp[0];
    }
};