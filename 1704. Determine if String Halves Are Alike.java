class Solution {
    public int cal(String s){
        int cnt = 0;
        for(int i=0;i<s.length();i++){
            if(s.charAt(i) == 'a' || s.charAt(i) == 'e' || s.charAt(i) == 'i' || s.charAt(i) == 'o' || s.charAt(i) == 'u'){
                cnt +=1;
            }
        }
        return cnt;
    }

    public boolean halvesAreAlike(String s) {
        int a = s.length();
        String s1 = s.substring(0,a/2);
        String s2 = s.substring(a/2,a);

        s1 = s1.toLowerCase();
        s2 = s2.toLowerCase();

        int a1 = cal(s1);
        int b1 = cal(s2);

        return a1==b1;
    }
}
