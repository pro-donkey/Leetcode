class Solution {
    public int fib(int n) {
        if(n == 1 || n == 0){
            return n;
        }
        return fib(n-1) + fib(n-2);
    }
}



// Using Dynamic Programming 
class Solution {
    public int fib(int n) {
        int [] arr = new int[n+1];
        return fib1(n,arr);
    }

    public int fib1(int n, int [] arr){
        if(n == 0 || n == 1){
            return n;
        }
        if(arr[n] != 0){
            return arr[n];

        }
        return fib1(n-1,arr) + fib1(n-2,arr);
    }
}
