import java.util.*;






public class Dior
{
    private static Scanner in = new Scanner(System.in);

    public static void main(String[] args) 
    {
        int n = in.nextInt();

        ArrayList<Long> arr = new ArrayList();
        for (int i = 0; i < n; i++)
            arr.add(in.nextLong());


        Collections.sort(arr);
        System.out.println(arr);
    }
}