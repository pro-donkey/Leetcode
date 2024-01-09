package Arrays;




public class secondLargest {
    public static int ssLargest(int [] arr){
        int largest = arr[0];
        int secondLargest = Integer.MIN_VALUE;

        for(int i=1;i<arr.length;i++){
            if(largest < arr[i]){
                secondLargest = largest;
                largest = arr[i];
            }

            else if(arr[i] < largest && arr[i] > secondLargest){
                secondLargest = arr[i];
            }
        }
        return secondLargest;
    }

    public static void main(String[] args) {

        int [] arr = {1,32,34,2,32,3,2};
        int ans = ssLargest(arr);
        System.out.println(ans);
    }
}
