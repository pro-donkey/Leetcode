class Solution {
    public long[] sumOfThree(long num) {
        if((num - 3) % 3 == 0){
            long a = ((num - 3)/3);
            return new long[]{a,a+1,a+2};
        }
        else return new long[]{};
    }
}
