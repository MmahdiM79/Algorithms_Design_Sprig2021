import java.util.*;






public class Dior
{
    private static Scanner in = new Scanner(System.in);
    private static long count = 0;



    public static void main(String[] args) 
    {
        int n = in.nextInt();

        ArrayList<Long> arr = new ArrayList<>();
        HashMap<Long, Integer> places = new HashMap<>();
        long hold;
        for (int i = 0; i < n; i++)
        {
            hold = in.nextLong();
            arr.add(hold);
            places.put(hold, i);
        }

        Collections.sort(arr);
        
    }
}