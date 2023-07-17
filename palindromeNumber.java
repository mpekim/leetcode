public class palindromeNumber {
   public static void main(String[] args) 
   {
      System.out.println("Please enter a number: ");
   }
   // Check to see if the number is a palindrome.
   // Currently, the number will be entered as a string.

   public static boolean isPalindrome(String num1, String num2){
      if (num1 == num2)
      {
         return true;
      }
      else
      {
         return false;
      }
   }
   public static String convertIntToString(int number)
   {
      String newString = toString(number);
      // Converts numbers into strings, as needed. (Can this be done with a typecast?)
      return newString;
   }
}
