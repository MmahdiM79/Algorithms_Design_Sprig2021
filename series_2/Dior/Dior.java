import java.util.Scanner






public class Dior
{
    private static Scanner in = new Scanner(System.in);
    public static void main(String[] args) 
    {
        long n = in.nextInt();

        long arr[n] = new long[n];
        for (int i = 0; i < n; i++)
            arr[i] = in.nextInt();

        long pivots = new long[n];
        for (int i = 0; i < n; i++)
            pivots[i] = in.nextInt();
    }
}