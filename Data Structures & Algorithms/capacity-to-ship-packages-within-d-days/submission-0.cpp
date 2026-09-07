class Solution {
    int calShipmentDays(vector<int>& weights, int curWeight){
        int res = 0;
        int reminder = 0;
        for (const auto& weight: weights){
            if (reminder + weight > curWeight){
                res += 1;
                reminder = weight;
            }
            else{
                reminder += weight;
            }
        }
        return (reminder == 0) ? res : res + 1;
    }
public:
    int shipWithinDays(vector<int>& weights, int days) {
        if (weights.empty() || days <= 0){
            return -1;
        }
        int left = *max_element(weights.begin(), weights.end());
        int right = accumulate(weights.begin(), weights.end(), 0);
        int mid = 0;
        int res = -1;
        while (left <= right){
            mid = left + ((right - left) / 2);
            if (calShipmentDays(weights, mid) <= days){
                res = mid;
                right = mid - 1;
            }
            else{
                left = mid + 1;
            }
        }
        return res;
    }
};