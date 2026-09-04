class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        vector<int> resTable ((amount + 1), INT_MAX);
        resTable[0] = 0;
        for (int curAmount = 1; curAmount <= amount; curAmount++){
            for (const auto& coin: coins){
                if (coin > curAmount || resTable[curAmount - coin] == INT_MAX){
                    continue;
                }
                resTable[curAmount] = min(resTable[curAmount], 1 + resTable[curAmount - coin]);
            }
        }
        return resTable[amount] == INT_MAX ? -1 : resTable[amount];
    }
};
