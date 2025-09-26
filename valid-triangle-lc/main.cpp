
// O(N^2 Logn) Solution
 
class Solution {
public:
    int triangleNumber(vector<int>& nums) {
        int n = nums.size();
        int cnt  = 0;
        sort(nums.begin(),nums.end());
        for(int i = 0 ; i < n-2 ; i++){
            for(int j = i+1 ; j < n-1 ; j++){
                int target = nums[i] + nums[j];
                int lo = j + 1 , hi = n - 1;
               
                while(lo <= hi){
                    int mid = (lo + hi)/2;
                    if(nums[mid] < target)
                        lo = mid + 1;
                    else
                    hi = mid - 1;
                }
                // cout <<"HIgh pointer is : "<< hi <<" low pointer is : " <<lo <<endl;
                cnt += hi - j;
            }

        }
        return cnt;
    }
};