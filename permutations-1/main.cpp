class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        queue<vector<int>> q;
        vector<vector<int>>result;
       
        q.push({});

        for(int i = 0 ; i < nums.size() ; i++){
            int sizeOfPerm = q.size();

            for(int j = 0 ; j < sizeOfPerm ; j++){
                vector<int> oldPerm = q.front();q.pop();

                for(int pos = 0 ; pos <= oldPerm.size() ; pos++){
                    vector<int>newPerm(oldPerm.begin(),oldPerm.end());
                    newPerm.insert(newPerm.begin()+pos,nums[i]);

                    if(newPerm.size() == nums.size())
                    result.push_back(newPerm);
                    else
                    q.push(newPerm);
                }
            }

        }
        return result;
    }
};