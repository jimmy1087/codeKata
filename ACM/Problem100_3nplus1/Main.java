package Problem100_3nplus1;

import java.io.*;
import java.util.*;

class Main {
	
	public static List<int[]> readCycleRanges() throws Exception {

	    List<int[]> cycleRanges = new ArrayList<>();
	    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	    String line = br.readLine();
	    while (!(line == null || line.trim().length() == 0)) {
	        StringTokenizer st = new StringTokenizer(line, " ");
	        int i = Integer.valueOf(st.nextToken());
	        int j = Integer.valueOf(st.nextToken());
	        cycleRanges.add(new int[] { i, j, 0 });
	        line = br.readLine();
	    }
	    return cycleRanges;
	}


	public static int current;
	public static int max;
	public static int counter;
	
	public static void main(String[] args) throws Exception {
		Main myWork = new Main();  
        myWork.Begin();            
    }
	
    void Begin() throws Exception
    {
		//long start = System.nanoTime(); // requires java 1.5
        String input;
        StringTokenizer idata;
        int a, b;
        
        List<int[]> cycleRanges = readCycleRanges();

        for( int[] inputLine : cycleRanges )
        {
          a = inputLine[0];
          b = inputLine[1];
          if (a<b) {
        	  max = handleInputs(a,b);
          } else {
        	  max = handleInputs(b,a);
          }
          System.out.println(a + " " + b + " " + max);
        }
        //double elapsedTimeInSec = (System.nanoTime() - start) * 1.0e-9;
        //System.out.println(elapsedTimeInSec);
    }	
	
	public static int handleInputs(int from, int to) {
		current = from;
		max = 0;
        while (current <= to) {
        	counter = 0;
        	solveByRecursion(current);
        	if (counter > max) {
        		max = counter;
        	}
        	current++;
        }
        return max;
	}
	
    
    public static String solveByRecursion(long number) {
        counter++;
        if (number <= 1)
            return "";
        if (number % 2 == 0)
            return solveByRecursion( number / 2 );
        else
            return solveByRecursion( number * 3 + 1 );
    }
}
