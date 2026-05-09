class Solution {
public:
    bool isAnagram(string s, string t) {

        if(s.size() != t.size()){
            return false;
        }

        int alpha[26] = {0};

        for(char c: s){
            alpha[c - 'a'] += 1;

        }

        for(char d : t){
            alpha[d - 'a'] -= 1;

        }

        for(int i =0;i<26;i++){
            if(alpha[i]!= 0 ){
                return false;
            }
        }
        return true;
    }
};
