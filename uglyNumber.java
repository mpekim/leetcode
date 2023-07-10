public class uglyNumber {
    public static void main(String [] args){
        System.out.println("Is the number 6 ugly?");
        System.out.println(uglyNumberCheck(6));
    }

    public static boolean uglyNumberCheck(int value){
        if (value <= 0){
            return false;
        }
        
        while (value % 2 == 0){
            value = value / 2;
        }

        while (value % 3 == 0){
            value = value / 3;
        }

        while (value % 5 == 0){
            value = value / 5;
        }

        if (value == 1){
            return true;
        }
        else{
            return false;
        }
    }
}
