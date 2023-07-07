public class oddInt
{
    public static void main(String[] args)
    {
        System.out.println("Odd number range between 3 and 7: ");
        System.out.println(oddIntCount(3, 7));
    }

    public static int oddIntCount(int low, int high){
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