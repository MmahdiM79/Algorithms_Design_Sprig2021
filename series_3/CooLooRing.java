import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Scanner;







public class CooLooRing
{
    private static Scanner in = new Scanner(System.in);
    private static int n, m, c;
    private static HashMap<Integer, ArrayList<Integer>> graph = new HashMap<>();
    private static int[] colorsV;

    private static ArrayList<Integer> g1;
    private static ArrayList<Integer> g2;
    private static long res = 0;

    private static long base = 1000000007;



    public static void main(String[] args) 
    {
        char kind = in.next().charAt(0);
        n = in.nextInt();
        c = in.nextInt();
        m = in.nextInt();


        if (kind == 'g')
        {
            colorsV = new int[n];

            for (int i = 0; i < n; i++)
            {
                colorsV[i] = -1;
                graph.put(i, new ArrayList<>());
            }

            for (int i = 0, u, v; i < m; i++)
            {
                u = in.nextInt()-1;
                v = in.nextInt()-1;

                graph.get(u).add(v);
                graph.get(v).add(u);
            }

            System.out.println(counterG(0) % base);
        }


        else if (kind == 'b')
        {
            HashSet<Integer> h1 = new HashSet<>();
            HashSet<Integer> h2 = new HashSet<>();

            colorsV = new int[n];
            for (int i = 0; i < n; i++)
            {
                colorsV[i] = -1;
                graph.put(i, new ArrayList<>());
            }

            for (int i = 0, u, v; i < m; i++)
            {
                u = in.nextInt()-1;
                v = in.nextInt()-1;

                h1.add(u); h2.add(v);

                graph.get(u).add(v);
                graph.get(v).add(u);
            }

            g1 = new ArrayList<>(h1);
            g2 = new ArrayList<>(h2);

            counterB1(g1, 0);
            System.out.println(res);
        }
            

        else // kind == 't'
        {
            long res = 1;
            for (int i = 0; i < n-1; i++)
            {
                res *= c-1;
                res %= base;
            }

            System.out.println((c*res) % base);
        }

    }



    private static long counterG(int currentV)
    {
        if (currentV == n)
            return 1;

        long sum = 0;
        for (int color = 0; color < c; color++)
            if (promising(color, currentV))
            {
                colorsV[currentV] = color;
                sum += counterG(currentV+1);
            }
              
        colorsV[currentV] = -1;
        return sum % base;
    }


    private static boolean promising(int color, int currentV)
    {
        for (int v : graph.get(currentV))
            if (colorsV[v] == color)
                return false;

        return true;
    }

    
    private static void counterB1(ArrayList<Integer> g, int currentV)
    {
        if (currentV >= g.size())
        {
            res += counterB2(g2);
            res %= base;
            return;
        }

        for (int color = 0; color < c; color++)
        {
            colorsV[g.get(currentV)] = color;
            counterB1(g, currentV+1);
        }
    }

    private static long counterB2(ArrayList<Integer> g)
    {
        long counter = 0;
        long out = 1;

        for(int v: g)
        {
            counter = 0;
            for (int color = 0; color < c; color++)
                if (promising(color, v))
                    counter++;

            out *= (counter);
            out %= base;
        }

        return out;
    }
}

