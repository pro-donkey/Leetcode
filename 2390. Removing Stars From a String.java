// This is very easy question want to skip skip it nothing special 

// Incase u want to optimize it you can use the string builder in java 






class Solution {
    public String removeStars(String s) {
        Stack<Character> stack = new Stack<>();
        for(Character it: s.toCharArray()){
            if(it != '*'){
                stack.push(it);
            }
            else if(it == '*'){
                stack.pop();
            }
        }

        String a = "";
        for(Character it : stack){
            a += it;
        }
        return a;
    }
}
