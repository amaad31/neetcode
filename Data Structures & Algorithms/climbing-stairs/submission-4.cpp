class Solution {
public:
    int climbStairs(int n) {
        if (n == 1){
            return 1;
        }
        int lastToLast = 1;
        int last = 2;
        for (int curStep = 3; curStep <= n; curStep++){
            int tmpLast = last;
            last = (last + lastToLast);
            lastToLast = tmpLast;
        }
        return last;
    }
};
