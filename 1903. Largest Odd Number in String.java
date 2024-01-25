class Solution {
    public String largestOddNumber(String s) {
        int n = s.length();
        int indx = -1;
        for(int i=n-1;i>-1;i--){
            if(s.charAt(i) == '1' || s.charAt(i) == '3' || s.charAt(i) == '5' || s.charAt(i) == '7' || s.charAt(i) == '9' ){
                indx = i;
                break;
            } 
        }
        if(indx == -1) return "";
        return s.substring(0,indx+1);
    }
}
