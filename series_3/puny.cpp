#include <iostream>
#include <vector>

using namespace std;




int main()
{
    int n, c;
    cin >> n >> c;

    vector<int> A(n, 0);
    for(int i = 0; i < n; i++)
        cin >> A[i];

    

    int min = A[0];
    int min_index = 0;

    int max = A[0];
    int max_index = 0;

    int first = 0;
    int last = 0;
    while(last < n)
    {
        if(max - min == c)
            break;
    
        else if(max - min > c)
        {
            if(min_index < max_index)
            {
                first = min_index + 1;
                min_index = first;
                min = A[first];

                for(int i = first + 1; i <= last; i++)
                    if(A[i] < min)
                    {
                        min = A[i];
                        min_index = i;
                    }
            }

            else // max_index < min_index
            { 
                first = max_index + 1;
                max_index = first;
                max = A[first];

                for(int i = first + 1; i <= last; i++)
                    if(A[i] > max)
                    {
                        max = A[i];
                        max_index = i;
                    }
            }
        }
        
        else // max - min < c
        { 
            last++;
            if(A[last] > max)
            {
                max = A[last];
                max_index = last;
            }

            if(A[last] < min)
            {
                min = A[last];
                min_index = last;
            }
        }
    }




    if(max - min == c)
    {
        if(min_index < max_index)
            cout << min_index + 1 << " " << max_index + 1 << endl;
        
        else
            cout << max_index + 1 << " " << min_index + 1 << endl;
    }
    else
        cout << -1 << endl;





    return 0;
}
