#include <string>
using namespace std;

class Solution {
public:
    string reverseWords(string s) {
        int left=0, right=0;
        string result = "";
        int N = s.size();

        for (int i=0; i<N; i++) {
            if (s[i] == ' ') {
                continue; 
            } else {
                left = i;
                while (i < N && s[i] != ' ') {
                    i++;
                }
                right = i; 

                string word = s.substr(left, right - left);

                if (result.empty()) {
                    result = word;
                } else {
                    result = word + " " + result;
                }
            }
        }
        return result;
    }
};