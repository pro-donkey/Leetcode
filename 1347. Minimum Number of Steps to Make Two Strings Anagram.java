class Solution {
    public int minSteps(String s, String t) {
        int [] hash1 = new int[27];
        int [] hash2 = new int[27];


        if(s.length() != t.length()) return -1;


        for(int i=0;i<s.length();i++){
            hash1[(int)s.charAt(i) - 96] += 1;
            hash2[(int)t.charAt(i) - 96] += 1;
        }


        int cnt = 0;
        for(int i=0;i<hash1.length;i++){
            cnt += Math.abs(hash1[i] - hash2[i]);
        }
        cnt /= 2;
        return cnt;
    }
}
