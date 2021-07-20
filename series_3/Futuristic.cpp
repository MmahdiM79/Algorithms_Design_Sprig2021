#include <iostream>
#include <cmath>
#include <vector>

using namespace std;




int main()
{
    int n;
    cin >> n;

    vector<int> A(n, 0);
    for(int i = 0; i < n; i++)
        cin >> A[i];
    
    int max = 0;
    for(int i = 0; i < n; i++)
        if(A[i] > max)
            max = A[i];
    

    int power = log2(max);
    int floor = pow(2, power);


    vector<int> candidates;
    for(int i = 0; i < n; i++)
        if(A[i] >= floor)
        {
            candidates.push_back(A[i]);
            A[i] = 0;
        }
    

    int can_size = candidates.size();
    int OR_result = 0;
    for(int i = 0; i < n; i++)
        OR_result = OR_result | A[i];
    

    int with_out_change = OR_result;
    for(int i = 0; i < can_size; i++)
        with_out_change = with_out_change | candidates[i];
    

    int max_res = with_out_change;
    int max_ind = -1;
    for(int i = 0; i < can_size; i++)
    {
        int temp =  with_out_change | (2 * candidates[i]);

        if(temp > max_res)
        {
            max_res = temp;
            max_ind = i;
        }
    }


    int final_res = OR_result;
    for(int i = 0; i < can_size; i++)
        if(i == max_ind)
            final_res = final_res | (2 * candidates[i]);
        else
            final_res = final_res | candidates[i];
          


    cout << final_res << endl;





    
    return 0;
}