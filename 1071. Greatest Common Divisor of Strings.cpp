class Solution {
public:
    string gcdOfStrings(string str1, string str2) {
        // so we have to observe an property that is 
        // str2 + str1 = str1 + str2  as we deal with gcd
        // ans will be substr(0.gcd(len1,len2)) or ""

        if(str1 + str2 == str2 + str1){
            return str1.substr(0,gcd(str1.length(),str2.length()));
        }
        return "";
    }
};
