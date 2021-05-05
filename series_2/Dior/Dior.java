import java.util.*;






public class Dior
{
    private static Scanner in = new Scanner(System.in);
    private static ArrayList<Long> arr = new ArrayList<>();
    private static long[] pivots;
    private static int placesIndex = -1;
    private static HashMap<Long, Integer> places = new HashMap<>();
    private static long count = 0;



    private static void solve(int p, int r)
    {
        if (r-p >= 1)
        {
            placesIndex++;
        }
        if (r-p <= 1)
            return;

        count += r - p - 1;
        int q = places.get(pivots[placesIndex]);
        solve(p, q);
        solve(q+1, r);
    }


    public static void main(String[] args) 
    {
        int n = in.nextInt();

        long hold;
        for (int i = 0; i < n; i++)
        {
            hold = in.nextLong();
            arr.add(hold);
            places.put(hold, i);
        }

        pivots = new long[n];
        for (int i = 0; i < n; i++)
            pivots[i] = in.nextLong();



        Collections.sort(arr);

        solve(0, n);
        
        System.out.println(count);
    }
}