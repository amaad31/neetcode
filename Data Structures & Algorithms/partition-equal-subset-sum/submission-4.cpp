class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int numsSum = accumulate(nums.begin(), nums.end(), 0);
        if (numsSum % 2 != 0){
            return false;
        }
        unordered_set<int> subSums;
        unordered_set<int> curSubSums;
        subSums.insert(0);
        for (int i = nums.size() - 1; i >= 0; i--) {
            for (const auto& subSum: subSums){
                curSubSums.insert(nums[i] + subSum);
            }
            subSums.insert(nums[i]);
            subSums.insert(curSubSums.begin(), curSubSums.end());
            curSubSums.clear();
        }
        return subSums.count((numsSum / 2));
    }
};
