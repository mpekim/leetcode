import java.util.Scanner;

public class Main {
    public static void main(String[] args){

        System.out.println("Welcome to the Java Leetcode program.");
        System.out.println("Please select a program to run: ");
        System.out.println("1. Odd Int");
        System.out.println("2. Palindrome Number");
        System.out.println("3. Two Sum");
        System.out.println("4. Ugly Number");

        Scanner input = new Scanner(System.in);
        int menuChoice = input.nextInt();

        switch(menuChoice)
        {
            case 1:
                oddInt o1 = new oddInt();
                o1.run();
                break;
            case 2:
                palindromeNumber p1 = new palindromeNumber();
                p1.run();
                break;
            case 3:
                twoSum t1 = new twoSum();
                t1.run();
                break;
            case 4:
                uglyNumber u1 = new uglyNumber();
                u1.run();
                break;
            default:
                System.out.println("I'm sorry, I do not understand that input.");
                break;
        }
    }
    // Driver function for the other leetcode classes.
}
