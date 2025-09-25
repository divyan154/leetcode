class Solution {
    // private:
    // int m, n;
    // int func(int i, int j , vector<vector<int>>& triangle,vector<vector<int>> &dp){
    //     if(i == n - 1)
    //     return triangle[i][j];
    //     if(dp[i][j] != -1)
    //     return dp[i][j];
    //     int leftSum = func(i+1,j,triangle,dp);
    //     int rightSum = func(i+1,j+1,triangle,dp);

    //     return dp[i][j] = (triangle[i][j] + min(leftSum, rightSum));
    // }
    public:
    int minimumTotal(vector<vector<int>>& triangle) {
         int n = triangle.size(), m = triangle[n-1].size();
         vector<vector<int>> dp(n,vector<int>(m,0));
         

         // Base case
         for(int j = 0 ; j < n ; j++){
            dp[n-1][j] = triangle[n-1][j];
         }

         for(int i = n-2 ; i >= 0 ; i-- ){
            for(int j = i ; j >= 0 ; j--){
                int left = dp[i+1][j];
                int right = dp[i+1][j+1];
                dp[i][j] = triangle[i][j] + min(left,right);
            }
         }

         return dp[0][0];

    }
};