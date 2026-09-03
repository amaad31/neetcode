class Solution {
public:
    int climbStairs(int n) {
        if (n == 1){
            return 1;
        }
        int lastToLast = 1;
        int last = 2;
        int res = 2;
        int curStep = 3;
        while (curStep <= n){
            res = (last + lastToLast);
            lastToLast = last;
            last = res;
            curStep++;
        }
        return res;
    }
};
