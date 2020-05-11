//     Author: Jaime Blanco
//     Github: github.com/jimmy1087
// HackerRank: hackerrank.com/jimmy1087

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int s = in.nextInt();
        int t = in.nextInt();
        int a = in.nextInt();
        int b = in.nextInt();
        int m = in.nextInt();
        int n = in.nextInt();
        
        int[] apple = new int[m];
        int applesInside = 0;
        for(int apple_i=0; apple_i < m; apple_i++){
            apple[apple_i] = in.nextInt();
            int d = a + apple[apple_i];
            if (d >= s && d <= t) {
                applesInside++;
            }
        }
        
        int[] orange = new int[n];
        int orangesInside = 0;
        for(int orange_i=0; orange_i < n; orange_i++){
            orange[orange_i] = in.nextInt();
            int d = b + orange[orange_i];
            if (d >= s && d <= t) {
                orangesInside++;
            }
        }
        
        System.out.println(applesInside);
        System.out.println(orangesInside);
    }
}
