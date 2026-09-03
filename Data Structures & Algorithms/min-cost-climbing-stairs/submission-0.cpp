class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        if (cost.size() == 0){
            return -1;
        }
        if (cost.size() == 1){
            return cost[0];
        }
        int lastToLast = cost[0];
        int last = cost[1];
        for (int i = 2; i < cost.size(); i++){
            int tmpLast = last;
            last = min(last + cost[i], lastToLast + cost[i]);
            lastToLast = tmpLast;
        }
        return min(last, lastToLast);
    }
};
