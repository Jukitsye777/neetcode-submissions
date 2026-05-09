class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        
        unordered_set <string> seen;
        
        for(int i= 0;i<board.size();i++){
            for(int j = 0;j<board.size();j++){
                
                char num = board[i][j];
                if(num == '.'){
                    continue;
                }

                string rowkey  = to_string(num) + "in row" + to_string(i);
                string colkey = to_string(num) + "in col" + to_string(j);
                string boxkey = to_string(num) + "in box" + to_string(i/3) + "-" + to_string(j/3);

                if(seen.count(rowkey) || seen.count(colkey) || seen.count(boxkey)){
                    return false;
                }
                seen.insert(rowkey);
                seen.insert(colkey);
                seen.insert(boxkey);


            }
        }

        return true;
    }
};