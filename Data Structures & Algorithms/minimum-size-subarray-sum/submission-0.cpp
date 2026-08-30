class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        if (nums.empty()){
            return 0;
        }

        int curRes = 0;
        int res = INT_MAX;
        int l = 0;
        for (int r = 0; r < nums.size(); r++){
            curRes += nums[r];
            while (curRes >= target){
                res = min(res, r - l + 1);
                curRes -= nums[l];
                l++;
            }
        }
        if (res == INT_MAX){
            return 0;
        }
        return res;
    }
};