// Arrays and Strings - 1.1 Unique Chars
// Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures ?
public class UniqueChars{

     public static void main(String []args){
        
        // Input string
        String str = "Helo mundi";
        System.out.println(str);
        
        // Call function
        if( hasUniqueChars(str) ) {
            System.out.println("Unique");
        }
        else
        {
            System.out.println("Repeated");
        }
     }
     
     // O(n^2)
     public static boolean hasUniqueChars(String str){
         
         for( int i = 0; i < str.length(); i++ ) {
             
             for( int j = 0; j < str.length(); j++ ) {
                 
                 if( i != j && str.charAt(i) == str.charAt(j) ) {
                     return false;
                 }
             }
         }
         
         return true;
     }
}
