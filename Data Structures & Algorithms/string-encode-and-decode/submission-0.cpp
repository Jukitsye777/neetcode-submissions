#include <vector>
#include <string>
using namespace std;

class Solution {
public:

    // Encode: use length + '#' + string
    string encode(vector<string>& strs) {
        string encoded;
        for (string &s : strs) {
            encoded += to_string(s.size()) + "#" + s;
        }
        return encoded;
    }

    // Decode: read length before '#' and extract string
    vector<string> decode(string s) {
        vector<string> result;
        int i = 0;
        while (i < s.size()) {
            int j = i;
            // Find the '#' to extract the length
            while (s[j] != '#') j++;
            int len = stoi(s.substr(i, j - i));  // convert length string to int
            result.push_back(s.substr(j + 1, len)); // extract string of given length
            i = j + 1 + len;  // move to next string
        }
        return result;
    }
};