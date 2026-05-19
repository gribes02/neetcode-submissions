class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        set<int> s;

        for (int i = 0; i < size(nums); i++) {
            if (s.count(nums[i]) > 0) {
                return true;
            }
            else {
                s.insert(nums[i]);
            }
        }

        return false;

    }
};