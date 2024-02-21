class Solution {
    
    public int robHouses(ArrayList<Integer> houseValues) {
        int[] dp = new int[houseValues.size()];
        int n = houseValues.size();
        dp[0] = houseValues.get(0);
        
        for (int i = 1; i < houseValues.size(); i++) {
            int currentHouseValue = houseValues.get(i);
            if (i > 1) {
                currentHouseValue += dp[i - 2];
            }
            int previousHouseValue = dp[i - 1];
            dp[i] = Math.max(currentHouseValue, previousHouseValue);
        }
        
        return dp[n - 1];
    }
    
    public int rob(int[] houseValues) {
        if (houseValues.length == 1) {
            return houseValues[0];
        }
        
        ArrayList<Integer> excludingFirstHouse = new ArrayList<>();
        ArrayList<Integer> excludingLastHouse = new ArrayList<>();
        
        for (int i = 0; i < houseValues.length; i++) {
            if (i != 0) {
                excludingFirstHouse.add(houseValues[i]);
            }
            if (i != houseValues.length - 1) {
                excludingLastHouse.add(houseValues[i]);
            }
        }
        
        int maxAmount1 = robHouses(excludingFirstHouse);
        int maxAmount2 = robHouses(excludingLastHouse);
        
        return Math.max(maxAmount1, maxAmount2);
    }
}
