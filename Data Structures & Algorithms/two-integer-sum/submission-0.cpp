#include <unordered_set>
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
    int diff = {0};
    unordered_set<int> seen;
    for (int i = 0; i < nums.size(); ++i ){
        diff = target - nums[i];
        if (seen.count(diff)) return {i, seen[diff]};
        seen[nums[i]] = i;
    }
    return {};
    }
};
