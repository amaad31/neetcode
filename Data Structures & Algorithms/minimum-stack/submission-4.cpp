class MinStack {
public:
    vector<int> minStack;
    vector<int> mins;
    MinStack() {}
    
    void push(int val) {
        minStack.push_back(val);
        if (mins.empty() || val <= mins.back()) {
            mins.push_back(val);
        }
    }
    
    void pop() {
        if (minStack.back() == mins.back()){
            mins.pop_back();
        }
        minStack.pop_back();
    }
    
    int top() {
        return minStack.back();
    }
    
    int getMin() {
        return mins.back();
    }
};
