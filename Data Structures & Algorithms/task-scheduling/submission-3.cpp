class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        unordered_map <char, int> tasksCount;
        for (const auto& task: tasks){
            tasksCount[task]++;
        }

        priority_queue<int> tasksPQ;
        for (const auto& pair: tasksCount){
            tasksPQ.push(pair.second);
        }

        queue<pair<int, int>> tasksWaitingQueue;
        int refTime = 0;
        while (!tasksWaitingQueue.empty() || !tasksPQ.empty()){
            if (!tasksWaitingQueue.empty() && tasksWaitingQueue.front().first == refTime) {
                tasksPQ.push(tasksWaitingQueue.front().second);
                tasksWaitingQueue.pop();
            }
            if (tasksPQ.empty()) {
                refTime = tasksWaitingQueue.front().first;
                continue;
            }
            int curTask = tasksPQ.top();
            tasksPQ.pop();
            curTask -= 1;
            if (curTask > 0){
                tasksWaitingQueue.push({refTime + n + 1, curTask});
            }
            refTime += 1;
        }
        return refTime;
    }
};
