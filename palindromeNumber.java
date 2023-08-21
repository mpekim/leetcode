import java.util.Scanner;

public class palindromeNumber {
   public void run() 
   {
      System.out.println("Please enter a number: ");
      Scanner input = new Scanner(System.in);

      int number = input.nextInt();
      String convertNumber = convertIntToString(number);

      System.out.println("Is " + convertNumber + " a palindrome? " + isPalindrome(convertNumber));
      input.close();
   }
   // Check to see if the number is a palindrome.
   // Currently, the number will be entered as a string.

   public boolean isPalindrome(String num1){
      // Fix logical check with self here.
      if (num1 == num1)
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
      String newString = "";

      while (number % 10 != 0)
      {
         newString = newString + (number % 10);
         number = number / 10;
      }

      System.out.println("New number string: " + newString);

      // Use a mod loop to get the digits.
      // Number is currently printed in reverse.
      return newString;
   }
}
