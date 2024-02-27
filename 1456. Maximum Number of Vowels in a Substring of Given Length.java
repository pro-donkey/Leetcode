class Solution {
    private boolean check(char a){
        if(a == 'a' || a == 'e' || a == 'i' || a=='o' || a=='u'){
            return true;
        }
        return false;
    }
    public int maxVowels(String s, int k) {
        int cnt = 0;
        int mx = 0;
        for(int i=0;i<s.length();i++){
            if(check(s.charAt(i))){
                cnt += 1;
            }
            if((i>=k) && (check(s.charAt(i-k)))){
                cnt-=1;
            }
            mx = Math.max(mx,cnt);
        }

        return mx;
    }
}
