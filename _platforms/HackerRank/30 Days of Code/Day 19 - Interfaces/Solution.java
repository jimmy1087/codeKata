//     Author: Jaime Blanco
//     Github: github.com/jimmy1087
// HackerRank: hackerrank.com/jimmy1087

// Other solutions
// Runtime: O(n^(1/2)) Space Complexity: O(1)
// https://www.hackerrank.com/challenges/30-interfaces/forum/comments/258725

import java.io.*;
import java.util.*;

interface AdvancedArithmetic {
   int divisorSum(int n);
}

class Calculator implements AdvancedArithmetic {
    
    // Recursive
    private int divisorSum(int n, int divisor) {
        if (divisor == 1) {
            return 1;
        }
        if (n%divisor == 0) {
            return divisor + divisorSum(n, divisor-1);
        } else {
            return divisorSum(n, divisor-1);
        }
    }
    
    public int divisorSum(int n) {
        return divisorSum(n, n);
    }
}

class Solution {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        scan.close();
        
        AdvancedArithmetic myCalculator = new Calculator(); 
        int sum = myCalculator.divisorSum(n);
        System.out.println("I implemented: " + myCalculator.getClass().getInterfaces()[0].getName() );
        System.out.println(sum);
    }
}
