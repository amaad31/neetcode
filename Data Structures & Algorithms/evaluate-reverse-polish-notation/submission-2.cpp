class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        unordered_set<string> operators = {"+", "-", "*", "/"};
        vector<int> numsStack;

        for (string token : tokens) {
            if (!operators.count(token)) {
                numsStack.push_back(stoi(token));
                continue;
            }

            int second_num = numsStack.back();
            numsStack.pop_back();

            int first_num = numsStack.back();
            numsStack.pop_back();

            if (token == "+") {
                numsStack.push_back(first_num + second_num);
            }
            else if (token == "-") {
                numsStack.push_back(first_num - second_num);
            }
            else if (token == "*") {
                numsStack.push_back(first_num * second_num);
            }
            else if (token == "/") {
                numsStack.push_back(first_num / second_num);
            }
        }

        return numsStack.back();
    }
};