class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int p1, p2, temp;
        //Below for loop makes p1 point to first 0 value in array
        for (int i=0; i<nums.size(); i++){ 
            if (nums[i]==0){
                p1 = i;
                p2 = i+1; //p2 initially is the value right after p1
                break;
            }
            else{
                continue;
            }
        }
        while(p2<nums.size()){
            if (nums[p2] != 0){ //If p2 points to non-zero int, swap it's value with p1
                temp=nums[p1];
                nums[p1]=nums[p2];
                nums[p2]=temp;
                p1++;
                p2++;
            }
            else{
                p2++;
            }
        }   
    }
};