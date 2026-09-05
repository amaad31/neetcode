class Solution {
    unordered_map<int, vector<int>> preqMap;
    bool checkPreqBFS(int targetPreq, int course){
        if (targetPreq == course){
            return true;
        }
        deque<int> courseQ;
        unordered_set<int> visitedCourses;
        courseQ.push_back(course);
        while (!courseQ.empty()){
            int curCourse = courseQ.front();
            courseQ.pop_front();
            for (const auto& curPreq: preqMap[curCourse]){
                if (curPreq == targetPreq){
                    return true;
                }
                if (!visitedCourses.count(curPreq)){
                    courseQ.push_back(curPreq);
                    visitedCourses.insert(curCourse);
                }
            }
        }
        return false;
    }
public:
    vector<bool> checkIfPrerequisite(int numCourses, vector<vector<int>>& prerequisites, vector<vector<int>>& queries) {
        for (const auto& preqArr: prerequisites){
           preqMap[preqArr[1]].push_back(preqArr[0]);
        }

        vector<bool> res;
        for (const auto& query: queries){
            res.push_back(checkPreqBFS(query[0], query[1]));
        }
        return res;
    }
};