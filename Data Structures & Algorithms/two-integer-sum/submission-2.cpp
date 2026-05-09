class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {


        int length = nums.size();
        vector <int> two;
        for(int i =0;i<length;i++){
            for(int j = i+1;j<length;j++){

                if(nums[i] + nums[j] == target){

                    two.push_back(i);
                    two.push_back(j);
                    return two;

                }

            }
        }

        
        
    }
};
