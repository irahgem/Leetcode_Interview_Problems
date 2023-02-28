// Given a sorted array of distinct integers and a target value, return the index if the target is found. 
// If not, return the index where it would be if it were inserted in order.

// You must write an algorithm with O(log n) runtime complexity.

// Example 1:

// Input: nums = [1,3,5,6], target = 5
// Output: 2

class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int left =0;
        int right = nums.size()-1;
        //Binary Search Algo
        while(left<= right){
            int mid = left + (right-left)/2;

            // if target is found return its index
            if(nums[mid] == target) return mid;

            else if(nums[mid] > target) right = mid-1;
            else left = mid+1;

        }
        //returning left index as it contains the position where it would be if it were inserted in order.
        return left;
    }
};