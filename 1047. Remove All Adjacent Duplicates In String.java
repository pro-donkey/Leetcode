class Solution {
    public String removeDuplicates(String s) {
        Stack<Character> stack = new Stack<>();
        for(Character it : s.toCharArray()){
            if(stack.isEmpty()){
                stack.push(it);
            }
            else if(stack.peek() == it){
                stack.pop();
            }
            else{
                stack.push(it);
            }
        
        }

        String ans = "";
        while(!stack.isEmpty()){
            ans = stack.pop() + ans;
        }
        return ans;
    }
}
