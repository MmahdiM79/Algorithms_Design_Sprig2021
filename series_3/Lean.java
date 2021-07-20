import java.util.ArrayList;
import java.util.Scanner;



public class Lean 
{
    private static Scanner in = new Scanner(System.in);

    private static  ArrayList<Long> times = new ArrayList<>();
    private static ArrayList<Long> works = new ArrayList<>();
    private static ArrayList<Double> rank = new ArrayList<>();


    public static void main(String[] args) 
    {
        int n = in.nextInt();

        for (int i = 0; i < n; i++)
            times.add(in.nextLong());

        for (int i = 0; i < n; i++)
            works.add(in.nextLong());



        for (int i = 0; i < n; i++)
            rank.add(works.get(i)/((double) times.get(i)));



        mergeSort(0, n-1);

        long total_t = 0;
        long total_c = 0;
        for (int i = 0; i < n; i++)
        {
            total_t += times.get(i);
            total_c += works.get(i) * total_t;
        }

        System.out.println(total_c);
    }








    public static void merge(int startIndex, int midIndex, int lastIndex)
    {

        int rightSubArraySize = midIndex - startIndex + 1;
        int leftSubArraySize = lastIndex - midIndex;



        long[] rightArrayT = new long[rightSubArraySize + 1];
        long[] rightArrayW = new long[rightSubArraySize + 1];
        double[] rightArrayR = new double[rightSubArraySize + 1];
        for (int i = 0; i < rightSubArraySize; i++)
        {
            rightArrayR[i] = rank.get(startIndex + i);
            rightArrayT[i] = times.get(startIndex + i);
            rightArrayW[i] = works.get(startIndex + i);
        }

        long[] leftArrayT = new long[leftSubArraySize + 1];
        long[] leftArrayW = new long[leftSubArraySize + 1];
        double[] leftArrayR = new double[leftSubArraySize + 1];
        for (int j = 0; j < leftSubArraySize; j++)
        {
            leftArrayR[j] = rank.get(midIndex + j + 1);
            leftArrayT[j] = times.get(midIndex + j + 1);
            leftArrayW[j] = works.get(midIndex + j + 1);
        }

        

        rightArrayT[rightSubArraySize] = Long.MIN_VALUE;
        rightArrayW[rightSubArraySize] = Long.MIN_VALUE;
        rightArrayR[rightSubArraySize] = Double.MIN_VALUE;
        leftArrayT[leftSubArraySize] = Long.MIN_VALUE;
        leftArrayW[leftSubArraySize] = Long.MIN_VALUE;
        leftArrayR[leftSubArraySize] = Double.MIN_VALUE;


        int i = 0, j = 0;
        for (int k = startIndex; k <= lastIndex; k++)
            if (rightArrayR[i] > leftArrayR[j])
            {
                rank.set(k, rightArrayR[i]);
                times.set(k, rightArrayT[i]);
                works.set(k, rightArrayW[i]);
                i++;
            }
            else
            {
                rank.set(k, leftArrayR[j]);
                times.set(k, leftArrayT[j]);
                works.set(k, leftArrayW[j]);
                j++;
            }
        }


    public static void mergeSort(int startIndex, int lastIndex)
    {
        if (startIndex < lastIndex)
        {
            int midIndex = (startIndex + lastIndex)/2;

            mergeSort(startIndex, midIndex);
            mergeSort(midIndex+1, lastIndex);

            merge(startIndex, midIndex, lastIndex);
        }
    }
}
