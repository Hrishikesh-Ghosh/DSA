class Solution {
public:
    bool isSubsequence(string s, string t) {
        int p1=0, p2=0;
        for(int i=0; i<t.size(); i++){
            if(s[p1] == t[p2]){
                p1++;
                p2++;
            }
            else{
                p2++;
            }
        }
        if(p1 == s.size()){
            return true;
        }
        else{
            return false;
        }
    }
};