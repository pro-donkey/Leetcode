class Solution {
    public int balancedStringSplit(String s) {
        int cnt = 0;
        int sm = 0;
        for(int i=0;i<s.length();i++){
            if(s.charAt(i) == 'L'){
                sm += 1;
            }
            else{
                sm -= 1;
            }
            if(sm == 0){
                cnt += 1;
            }
        }
        return cnt;
    }
}
