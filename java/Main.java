import java.util.*;

public class Main {
    public static void main(String[] args){
        boolean continueProgram = true;

        while (continueProgram == true)
        {
            runProgram();
            continueProgram = continueCheck();
        }
    }

        public static void runProgram(){
            System.out.println("Welcome to the Java Leetcode program.");
            System.out.println("Please select a program to run: ");
            System.out.println("1. Odd Int");
            System.out.println("2. Palindrome Number");
            System.out.println("3. Two Sum");
            System.out.println("4. Ugly Number");
    
            Scanner input = new Scanner(System.in);
            // Figure out how to properly close Scanners.
            int menuChoice = input.nextInt();
    
            switch(menuChoice)
            {
                case 1:
                    oddInt o1 = oddInt.getInstance();
                    o1.run();
                    break;
                case 2:
                    palindromeNumber p1 = palindromeNumber.getInstance();
                    p1.run();
                    break;
                case 3:
                    twoSum t1 = twoSum.getInstance();
                    t1.run();
                    break;
                case 4:
                    uglyNumber u1 = uglyNumber.getInstance();
                    u1.run();
                    break;
                default:
                    System.out.println("I'm sorry, I do not understand that input.");
                    break;
            }
    }

    public static boolean continueCheck()
            {
                System.out.println("Would you like to continue? [y/n]:");
                Scanner result = new Scanner(System.in);
                String answer = result.nextLine();

                switch (answer)
                {
                    case "y":
                    case "Y":
                        return true;
                    case "n":
                    case "N":
                        return false;
                    default:
                        System.out.println("I'm sorry, I do not understand that input.");
                        System.out.println("Resorting to default answer (no).");
                        return false;
                }
            }
    // Driver function for the other leetcode classes.

}
