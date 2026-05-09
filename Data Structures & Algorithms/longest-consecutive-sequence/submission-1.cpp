class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set <int> numset(nums.begin(),nums.end());
     
        int longeststreak = 0;


        for(int num :nums){
            int currentnum = 0;
            int streak = 0;
            if(numset.find(num-1)==numset.end()){
                 currentnum = num;
                streak = 1;


                         while(numset.find(currentnum+1) != numset.end()){
                streak += 1;
                currentnum += 1;

            }
            longeststreak = max(longeststreak,streak);

            }

   

        }

        return longeststreak;
        
    }
};
