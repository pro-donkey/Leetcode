class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        int sz1 = g.size();
        int sz2  = s.size();

        sort(g.begin(),g.end());
        sort(s.begin(),s.end());

        int greed = sz1 - 1;
        int cookie = sz2 - 1;
        int cnt = 0;
        while(greed >= 0 && cookie >= 0){
            if(s[cookie] >= g[greed]){
                cnt +=1 ;
                greed--;
                cookie--;

            }
            else {
                greed --;
            }
        }
        return cnt;
    }
};
