// Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
// You must implement a solution with a linear runtime complexity and use only constant extra space.

// Example 1:

// Input: nums = [2,2,1]
// Output: 1

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        map<int, int> s;
        for(auto it : nums){
            s[it]++;
        }
        for(auto it : s){
            if(it.second == 1){
                return it.first;
            }
        }
        return 0;
    }
};