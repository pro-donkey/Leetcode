class Solution {
    public boolean uniqueOccurrences(int[] arr) {
        HashSet<Integer> set = new HashSet<>();
        HashMap<Integer,Integer> map = new HashMap<>();
        for(int i=0;i<arr.length;i++){
            if(map.containsKey(arr[i])){
                map.put(arr[i],map.get(arr[i]) + 1);
            }
            else {
                map.put(arr[i],1);
            }

        }

        for(Integer it : map.values()){
            if(set.contains(it)){
                return false;
            }
            else {
                set.add(it);
            }
        }
        return true;
    }
}
