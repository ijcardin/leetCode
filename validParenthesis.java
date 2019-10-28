class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        char upper = '\0';

        for(int i = 0; i < s.length(); i++){
            if(stack.isEmpty() == false)
                upper = stack.peek();
            stack.push(s.charAt(i));
            if(stack.size() > 1){
                if((upper == '(' && stack.peek() == ')') ||
                    (upper == '{' && stack.peek() == '}') ||
                    (upper == '[' && stack.peek() == ']')) {
                        stack.pop();
                        stack.pop();
                    }
            }
        }
        return stack.isEmpty() ? true : false;
    }
}
