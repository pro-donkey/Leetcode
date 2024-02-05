class Solution {
    public boolean check(char a) {
        if (a == 'a' || a == 'e' || a == 'i' || a == 'o' || a == 'u' || a == 'A' || a == 'E' || a == 'I' || a == 'O'
                || a == 'U') {
            return true;
        }
        return false;
    }

    public String reverseVowels(String s) {
        char[] arr = s.toCharArray();
        int left = 0;
        int right = arr.length - 1;
        while (left <= right) {
            if ((check(arr[left]) && (check(arr[right])))) {
                char temp = arr[left];
                arr[left] = arr[right];
                arr[right] = temp;
                right--;
                left++;
            } else if (check(arr[left])) {
                right--;
            } else if (check(arr[right])) {
                left++;
            } else {
                left++;
                right--;
            }
        }

        return new String(arr);
    }
}
