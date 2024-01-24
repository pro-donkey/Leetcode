class Solution {
    public String interpret(String command) {
        StringBuilder j = new StringBuilder();
        int i;
        for(i=0;i<command.length();i++){
            if(command.charAt(i)=='G'){
                j.append('G');
            }else if(command.charAt(i)=='('){
                if(command.charAt(i+1)==')'){
                    j.append('o');
                }else{
                    j.append('a');
                    j.append('l');
                }
            }
        }
        return j.toString();
    }
}
