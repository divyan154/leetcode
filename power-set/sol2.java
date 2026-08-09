// Using Recursion ---- Pick/ Non Pick Approach
// Backtracking

import java.util.ArrayList;

class Solution{
    private String s;
    int n;
    ArrayList<String>subsequences;

    Solution(String s){
        this.s = s;
        subsequences = new ArrayList<>();
        n = s.length();
    }

    private void printSubsequenceByRecursion(StringBuilder temp, int index){
        // Base Case
        if (index == n){
            subsequences.add(temp.toString());
            return;
        }
        System.out.println(temp);

        temp.append(s.charAt(index));
        printSubsequenceByRecursion(temp, index+1);
        temp.deleteCharAt(temp.length()-1);
        printSubsequenceByRecursion(temp, index+1);

    }

    public ArrayList<String> main(){
        StringBuilder temp = new StringBuilder();
        printSubsequenceByRecursion(temp, 0);
        return subsequences;
    }

}

public class sol2 {
    public static void main(String[] args) {
        String s = "abc";
        Solution solution = new Solution(s);
        ArrayList<String> res = solution.main();
        System.out.println(res);
    }
}

