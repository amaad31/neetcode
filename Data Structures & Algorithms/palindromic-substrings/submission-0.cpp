class Solution {
public:
    int countSubstrings(string s) {
        int res = 0;

        for (int i = 0; i < s.size(); i++){
            // odd len
            int leftPtr = i;
            int rightPtr = i;
            while(leftPtr >= 0 && rightPtr < s.size() && s[leftPtr] == s[rightPtr]){
                res += 1;
                leftPtr -= 1;
                rightPtr += 1;
            }
            
            // even len
            leftPtr = i;
            rightPtr = i + 1;
            while(leftPtr >= 0 && rightPtr < s.size() && s[leftPtr] == s[rightPtr]){
                res += 1;
                leftPtr -= 1;
                rightPtr += 1;
            }
        }
        return res;
    }
};
