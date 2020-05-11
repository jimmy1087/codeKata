//     Author: Jaime Blanco
//     Github: github.com/jimmy1087
// HackerRank: hackerrank.com/jimmy1087

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    static int[] solve(int[] grades){
        int[] results = new int[grades.length];
        for (int i = 0; i<grades.length; i++) {
            int value = grades[i];
            if (value < 38) {
                results[i] = value;
            } else {
                int remainder = value % 5;
                if (5-remainder < 3) {
                    results[i] = value + 5-remainder;
                } else {
                    results[i] = value;
                }
            }
        }
        return results;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[] grades = new int[n];
        for(int grades_i=0; grades_i < n; grades_i++){
            grades[grades_i] = in.nextInt();
        }
        int[] result = solve(grades);
        for (int i = 0; i < result.length; i++) {
            System.out.print(result[i] + (i != result.length - 1 ? "\n" : ""));
        }
        System.out.println("");
    }
}
