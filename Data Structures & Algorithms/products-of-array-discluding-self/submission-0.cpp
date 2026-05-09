class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector <int>resultsl(n,1);
        vector <int>resultsr(n,1);

        int left = 1;
        for(int i =0;i<resultsl.size();i++){
            
            resultsl[i] = left;
            left = left*nums[i];

        }
        int right = 1;
        for(int i =n-1;i>=0;i--){
            resultsr[i] = right;
            right = right*nums[i];

        }
        

        for(int i =0;i<n;i++){
            resultsl[i] *= resultsr[i];

        }

        return resultsl;
    }
};