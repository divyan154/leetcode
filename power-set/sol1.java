// Using Bitmasking 
// Take every possible subset upto 2^n and compare its digits 
// if it is 1 then add that char in ans , else not 

import java.util.ArrayList;

class Solution{
    private String s;
    ArrayList<String>subsequences ;

    Solution(String s){
        this.s = s;
        this.subsequences = new ArrayList<>();

    }

    public ArrayList<String> main(){
        int n = s.length();
        int total = 1 << n;
      
        for( int mask = 0 ; mask < total ; mask++){
              StringBuilder res = new StringBuilder();
            for (int i = 0 ; i < n ; i++){
                if (((mask) &  (1<<i)) != 0){
                    res.append(s.charAt(i));
                }
            }
            subsequences.add(res.toString());

        }
        return subsequences;


    }


    
 }


public class sol1 {
    static void main(){
        String s = "abcd";
        new ArrayList<>();
        Solution solution = new Solution(s);
        ArrayList<String> ans = solution.main();
        System.out.println(ans) ;

    }
}


// Time complexity -- O(N*2^N)
// Space COmplexity -- O(N*2^N)