class Solution {
    public int calculate(int a, int b, String c) {
        switch (c) {
            case "+":
                return a + b;
            case "*":
                return a * b;
            case "/":
                return a / b;
            default:
                return a - b;
        }
    }

    public boolean checkSign(String it) {
        return it.equals("+") || it.equals("-") || it.equals("/") || it.equals("*");
    }

    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>();
        for (int i = 0; i < tokens.length; i++) {
            if (checkSign(tokens[i])) {
                int b = stack.pop();
                int a = stack.pop();
                int result = calculate(a, b, tokens[i]);
                stack.push(result);
            } else {
                stack.push(Integer.parseInt(tokens[i]));
            }
        }
        return stack.peek();
    }
}
