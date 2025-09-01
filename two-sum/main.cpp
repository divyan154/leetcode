class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> mpp ; // store prev ocurrence of element alonh with inde
        vector <int> ans;
        for(int i = 0 ; i < nums.size() ; i++){
            if(i == 0)
            mpp[nums[i]] = i;
            else{
                int x = target - nums[i];
                if(mpp.find(x) != mpp.end()){
                   return {mpp[x],i};

                }
                else
                mpp[nums[i]] = i;

            }
        }
        return ans;
    }
};