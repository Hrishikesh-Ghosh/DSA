class Solution {
public:
    bool isPalindrome(string s) {
        int p1=0, p2=s.length()-1;
        while(p2>p1){
            if(!isalnum(s[p1])){
                p1++;
            }
            else if(!isalnum(s[p2])){
                p2--;
            }
            else{
                if(tolower(s[p1])==tolower(s[p2])){
                    p1++;
                    p2--;
                }else{
                    return false;
                }
            }
        }
        return true;
    }
};