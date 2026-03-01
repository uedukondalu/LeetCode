class Solution {
    public boolean isPalindrome(int x) {
        
        String str=Integer.toString(x);
        StringBuilder s=new StringBuilder(str);
        s.reverse();
        String st=s.toString();
        return str.equals(st);
    }
}