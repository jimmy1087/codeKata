//******************************************************************
//                                                                 
//  Problem3nplus1.java                                               
//                                                                 
// ******************************************************************

package Problem100_3nplus1;

public class Problem3nplus1
{
	
	public static int counter = 0;
	public static int from = 201;
	public static int to = 210;
	public static int current;
	public static int max;

    public static void main( String[] args )
    {
        
    	long start = System.nanoTime(); // requires java 1.5
    	// Segment to monitor
    	
        while (from <= to) {
        	counter = 0;
        	current = from++;
        	System.out.println("Process: " + current);
        	solveByRecursion(current);
        	System.out.println("Cycle: " + counter);
        	if (counter > max) {
        		max = counter;
        	}
        }
        
        double elapsedTimeInSec = (System.nanoTime() - start) * 1.0e-9;
        
        System.out.println(elapsedTimeInSec);
        System.out.println("Max cycle length: " + max);
    }
    
    public static String solveByRecursion(long number) {
        
        //System.out.println(String.valueOf( number ));
        
        counter++;
        
        if (number <= 1)
            return "";
        if (number % 2 == 0)
            return solveByRecursion( number / 2 );
        else
            return solveByRecursion( number * 3 + 1 );
    }
        
}


