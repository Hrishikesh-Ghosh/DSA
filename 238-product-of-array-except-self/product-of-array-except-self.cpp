#include <vector>
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
       vector<int> left(nums.size());
       vector<int> right(nums.size());
       vector<int> answer(nums.size());
       left[0]=1;
       for (int i=1; i<left.size(); i++){
            left[i]=nums[i-1]*left[i-1];
       }    
       right[nums.size()-1]=1;
       for (int j=nums.size()-2; j>=0; j--){
            right[j]=nums[j+1]*right[j+1];
       }
       for(int k=0; k<nums.size(); k++){
            answer[k]=left[k]*right[k];
       }
       return answer;
    }
};