class Solution {
public:
    bool isAnagram(string s, string t) {
        map<char, int> string_s;
        map<char, int> string_t;

        for(int i=0; i < s.size(); i++){
            char current_char = s[i];
            string_s[current_char]++;
        }

        for(int i=0; i < t.size(); i++){
            char current_char = t[i];
            string_t[current_char]++;
        }

        if(string_t == string_s){
            return true; 
        }

        return false;

    }
};
