class Solution {
    public int areaOfMaxDiagonal(int[][] dim) {
        int mx = 0;
        int t = 0;
        int ans = 0;
        for(int i=0;i<dim.length;i++){
            t = dim[i][0]*dim[i][0] + dim[i][1]*dim[i][1];
            if(t > mx){
                mx = t;
                ans = dim[i][0] * dim[i][1];
            }
            else if(t == mx){
                mx = t;
                ans = Math.max(ans,dim[i][0]*dim[i][1]); 
            }
        }
        return ans;
    }
}
