class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_set<int> seen(nums.begin(), nums.end());

        return seen.size() != nums.size();
        
    }
};