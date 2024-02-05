class Solution {
    public int firstUniqChar(String s) {
        HashMap<Character, Integer> map = new HashMap<>();
        for(Character it: s.toCharArray()){
            if(map.containsKey(it)){
                map.put(it,map.get(it)+1);
            }
            else{
                map.put(it,1);
            }
        }

        for(int i=0;i<s.length();i++){
            if(map.get(s.charAt(i)) == 1){
                return i;
            }
        }
        return -1;
    }
}




// other solution 
class Solution {
     public int firstUniqChar(String s) {
        int ans = Integer.MAX_VALUE;
        for(char c='a'; c<='z';c++){
            int index = s.indexOf(c);
            if(index!=-1&&index==s.lastIndexOf(c)){
                ans = Math.min(ans,index);
            }
        }
        return ans==Integer.MAX_VALUE?-1:ans;
    }   
}
