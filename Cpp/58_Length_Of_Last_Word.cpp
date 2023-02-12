// Given a string s consisting of words and spaces, return the length of the last word in the string.

// A word is a maximal substring consisting of non-space characters only.

// Example 1:

// Input: s = "Hello World"
// Output: 5
// Explanation: The last word is "World" with length 5.

class Solution {
public:
    int lengthOfLastWord(string s) {
        int n=s.size();
        int cnt=0;
        for(int i=n-1;i>=0;i--)
        {
            if (isspace(s.at(i)) && cnt>0) break;
            else
            {
                if (isspace(s.at(i)) && cnt==0) continue;
                else cnt++;
            }
        }
        return cnt;
    }
};