class Solution {
    public int numRescueBoats(int[] people, int limit) {
        int n = people.length;
        int cnt = 0;
        int left = 0;
        int right = n - 1;
        Arrays.sort(people);
        while(left <= right){
            if(people[left] + people[right] <= limit){
                left += 1;
                right -= 1;
                cnt += 1;
            }
            else {
                right -= 1;
                cnt += 1;
            }
        }
        return cnt;
    }
}


// below is the python solution as well 
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        people.sort()
        cnt = 0
        left , right = 0, n-1
        while left <= right :
            if people[left] + people[right] <= limit:
                left += 1
                right -= 1
                cnt += 1

            else :
                right -= 1
                cnt += 1
        
        return cnt
