class Solution {
    // private:
    // int func(int i , int j , vector <int>&values, vector <vector<int>>&dp){
    //     if(dp[i][j] != -1)
    //     return dp[i][j];
    //     int res = 0 ;
    //     for(int k = i + 1 ; k < j ; k++){
    //         res = min(res == 0 ? INT_MAX: res,(values[i]*values[k]*values[j]) + func(i,k,values,dp) + func(k,j,values,dp));
    //     }
    // return dp[i][j] = res;
    // }
public:
    int minScoreTriangulation(vector<int>& values) {
        int n = values.size();
        vector <vector<int>>dp(n,vector<int>(n,0));
        
        for(int i = n - 1 ; i >= 0 ; i--){
            for(int j = i + 1 ; j < n ; j++){
                 int res = 0 ;
                 for(int k = i + 1 ; k < j ; k++){
                    res = min(res == 0 ? INT_MAX:res,values[i]*values[k]*values[j] + dp[i][k] + dp[k][j]);
                 }
                 dp[i][j] = res;
  
   
            }
        }
        return dp[0][n-1];

    }
};