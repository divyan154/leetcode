class Solution {
    private:
    int solve(int ind, vector<int>nums,int n,vector<int>&dp){
        if(ind == n)
        return 0;
        if(dp[ind] != -1)
        return dp[ind];
        int pick = nums[ind];
        if(ind+2 < n)
         pick  += solve(ind+2,nums,n,dp);
        int npick = solve(ind+1,nums,n,dp);
        return dp[ind] = max(pick,npick);

    }
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        vector <int>dp(n,-1);
        return solve(0,nums,n,dp);
    }
};