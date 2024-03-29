import java.util.*;

public class twoSum {

    private static twoSum instance;

    public static twoSum getInstance(){
        if (instance == null){
            instance = new twoSum();
        }
        return instance;
    }

    private twoSum(){

    }

    public void run(){
        
        System.out.println("Welcome to the TwoSum program.");

        int[] arr = {2, 3, 4, 5};
        int[] solution = findTwoSum(arr, 5);
        // Research why arrays must always be initialized
        // when declared.

        presentSolution(solution[0], solution[1]);
    }

    public int[] findTwoSum(int[] list, int answer){

        for (int i = 0; i < list.length; i++)
        {
            for (int j = i + 1; j < list.length; j++)
            {
                if (list[i] + list[j] == answer)
                {
                    System.out.println("Solution found.");

                    int[] solution = {list[i], list[j]};

                    return solution;
                }
            }
        }

        int[] solution = {-1, -1};
        // Present this solution as "error code".

        return solution;
    }

    public static void presentSolution(int sol1, int sol2){
        System.out.println("Solution to TwoSum: " + "[" + sol1 + "," + sol2 + "]");
    }
}
