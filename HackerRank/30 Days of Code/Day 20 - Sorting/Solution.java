//     Author: Jaime Blanco
//     Github: github.com/jimmy1087
// HackerRank: hackerrank.com/jimmy1087

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
    
    public int numSwaps = 0;
    public int firstElement = 0;
    public int lastElement = 0;
    
    public void sortArrayWithBubbleSort(int[] a) {
        for (int outer = 0; outer < a.length; outer++) {
            for (int inside = a.length-1; inside >= outer+1; inside--) {
                if (a[inside] < a[inside-1] ) {
                    int tmp = a[inside-1];
                    a[inside-1] = a[inside];
                    a[inside] = tmp;
                    numSwaps++;
                }
            }
        }
        firstElement = a[0];
        lastElement = a[a.length-1];
    }
    

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[] a = new int[n];
        for(int a_i=0; a_i < n; a_i++){
            a[a_i] = in.nextInt();
        }
        
        // Solve
        Solution solution = new Solution();
        solution.sortArrayWithBubbleSort(a);
        
        // Print
        System.out.println("Array is sorted in " + solution.numSwaps + " swaps.");
        System.out.println("First Element: " + solution.firstElement);
        System.out.println("Last Element: " + solution.lastElement);
    }
}
