public class NumStudUte {
    private static NumStudUte instance;

    public static NumStudUte getInstance(){
        if (instance == null){
            instance = new NumStudUte();
        }
        return instance;
    }

    private NumStudUte(){

    }

    public void run(){
        System.out.println("Determining the number of studentsunable to eat:");
        
    }

    public int determineEatCount(){
        int students[] = {0, 1, 0, 1};
        int sandwiches[] = {1, 0, 1, 0};

        int total = students.length;
        int top = sandwiches[0];
        int eat = 0;

        return (total - eat);
    }
}
