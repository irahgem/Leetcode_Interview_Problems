// Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
// The overall run time complexity should be O(log (m+n)).

// Example 1:

// Input: nums1 = [1,3], nums2 = [2]
// Output: 2.00000
// Explanation: merged array = [1,2,3] and median is 2.

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        vector<int>med;
        for(int i=0; i<nums1.size();i++)
            med.push_back(nums1[i]);
        for(int j=0; j<nums2.size();j++)
            med.push_back(nums2[j]);
        sort(med.begin(), med.end());

        double m = med.size(), c, f, ans, d;
        if (med.size() % 2 == 0)
        {
            d=m/2;
            c = med[d];
            f = med[d-1];
            ans = (c+f)/2;
        }
        else
        {
            ans = med[m/2];
        }
        
        return ans;

    }
};