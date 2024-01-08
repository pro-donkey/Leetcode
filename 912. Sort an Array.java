// the code is done using mergeSort





class Solution {

    public void merge(int []arr , int low , int mid , int high){
        ArrayList<Integer> store = new ArrayList<>();

        
        int left = low;
        int right = mid + 1;

        while((left <= mid)&&(right <= high)){
            if(arr[left] <= arr[right]){
                store.add(arr[left]);
                left ++;
            }
            else{
                store.add(arr[right]);
                right++;
            }
        }

        while(left <= mid){
            store.add(arr[left]);
            left++;
        }
        while(right <= high){
            store.add(arr[right]);
            right ++;
        }

        for(int i=low;i<=high;i++){
            arr[i] = store.get(i-low);
        }
    }



    public void mergeSort(int [] arr, int low, int high){
        if(low >= high) return ;
        int mid = (low + high)/2;
        mergeSort(arr, low , mid);
        mergeSort(arr, mid + 1, high);
        merge(arr,low,mid,high);
    }

    public int[] sortArray(int[] nums) {
        int high = nums.length-1;
        int low = 0;
        mergeSort(nums,low,high);
        return nums;
    }
}
