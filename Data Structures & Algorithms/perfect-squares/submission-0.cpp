class Solution {
public:
    int numSquares(int n) {
        vector<int> perfectSqs;
        int curPerSq = 1;
        while ((curPerSq * curPerSq) <= n){
            perfectSqs.push_back(curPerSq * curPerSq);
            curPerSq += 1;
        }
        vector<int> resTable (n + 1, INT_MAX);
        resTable[0] = 0;
        for (int curTarget = 1; curTarget <= n; curTarget++){
            for (const auto& curPerSq: perfectSqs){
                if (curPerSq > curTarget) continue; 
                resTable[curTarget] = min(resTable[curTarget], 1 + resTable[curTarget - curPerSq]);
            }
        }
        return resTable[n];
    }
};