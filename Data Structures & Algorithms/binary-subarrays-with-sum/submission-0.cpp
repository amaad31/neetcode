class Solution {
    int subarraysUpToK(vector<int>& nums, int target){
        if (target < 0){
            return 0;
        }
        int sum = 0;
        int res = 0;
        int l = 0;
        int r = 0;
        while (r < nums.size()){
            sum += nums[r];
            while (sum > target){
                sum = sum - nums[l];
                l += 1;
            }
            res += (r - l + 1);
            r += 1;
        }
        return res;
    }
public:
    int numSubarraysWithSum(vector<int>& nums, int goal) {
        return subarraysUpToK(nums, goal) - subarraysUpToK(nums, (goal - 1));
    }
};