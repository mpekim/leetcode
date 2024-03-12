import java.util.*;

public class oddInt
{
    private static oddInt instance;

    public static oddInt getInstance(){
        if (instance == null){
            instance = new oddInt();
        }
        return instance;
    }
    
    private oddInt(){

    }

    public void run()
    {
        System.out.println("Odd number range between 3 and 7: ");
        System.out.println(oddIntCount(3, 7));

        // Create functions that allow the user to accept input.
        Scanner input = new Scanner(System.in);
        // Figure out how to properly close Scanners.

        System.out.println("Please enter a value for the lower boundary: ");
        int low = input.nextInt();

        System.out.println("Please enter a value for the upper boundary: ");
        int high = input.nextInt();

        System.out.println("Odd number count between " + low + " and " + high + ": " + oddIntCount(low, high));
    }

    public int oddIntCount(int low, int high){
            if (low % 2 == 1)
            {
                low--;
            }
            if (high % 2 == 1)
            {
                high++;
            }
            return (high - low) / 2;
        }
}