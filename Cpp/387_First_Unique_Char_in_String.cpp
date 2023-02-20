// Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

// Example 1:

// Input: s = "leetcode"
// Output: 0


class Solution {
public:
    int firstUniqChar(string s) {
        map<char, int> hash;
        for (int i=0; i < s.size(); i++) 
        { 
            hash[s[i]]++;
        } 
        
        for (int i=0; i < s.size(); i++) 
        {
            if (hash[s[i]] == 1)
                return i;
        } 
        return -1;
    }
};