// Given an integer x, return true if x is a palindrome, and false otherwise.
// Example 1:

// Input: x = 121
// Output: true
// Explanation: 121 reads as 121 from left to right and from right to left.

using namespace std;
class Solution {
public:
    bool isPalindrome(int x) {
        string str = to_string(x);
    
        reverse(str.begin(), str.end());
    
        // converting string to integer
        int num = stoll(str);

        if (x == num){
            return true;
        }
        else{
            return false;
        }
    }
};