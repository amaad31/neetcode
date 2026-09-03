class Solution {
public:
    int rob(vector<int>& nums) {
        if (nums.size() <= 3){
            return *max_element(nums.begin(), nums.end());
        }

        // Without the last element
        int lastToLast = nums[0];
        int last = nums[1];
        for (int i = 2; i < nums.size() - 1; i++){
            int tmpLast = last;
            last = max(nums[i] + lastToLast, last);
            lastToLast = max(tmpLast, lastToLast);
        }
        int resWOLast = last;

        // Without the first element
        lastToLast = nums[1];
        last = nums[2];
        for (int i = 3; i < nums.size(); i++){
            int tmpLast = last;
            last = max(nums[i] + lastToLast, last);
            lastToLast = max(tmpLast, lastToLast);
        }
        return max(last, resWOLast);
    }
};
