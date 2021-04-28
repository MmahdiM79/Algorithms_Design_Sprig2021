









from typing import Counter


if __name__ == "__main__":

    n = int(input())

    array = [int(x) for x in input().split()]
    array.sort()

    Max = max(array)
    Min = min(array)



    num_questions = int(input())


    lower = 0; equal = 0; greater = 0

    for _ in range(num_questions):

        curr = int(input())
        if curr < Min:
            print(f'0 0 {n}')
            continue
        if curr > Max:
            print(f'{n} 0 0')
            continue


        start, end = 0, len(array)-1
        m = 2
    
        while True:
        
            mid = (end + start)//2
            

            if array[mid] == curr:
                equal += 1
                if lower == 0:
                    lower = n//m
                if greater == 0:
                    greater = n//m

                equal_r = 0
                for i in range(mid+1, n):
                    if array[i] != curr:
                        break
                    else:
                        equal_r += 1

                equal += equal_r
                greater -= equal_r


                equal_l = 0
                for j in range(mid-1, -1, -1):
                    if array[j] != curr:
                        break
                    else:
                        equal_l += 1

                equal += equal_l
                lower -= equal_l


                break
                    

            
            if start == :
                break

            if curr > array[mid]:
                lower += n//m + 1
                start = mid
            else:
                greater += n//m + 1
                end = mid

            m *= 2




        print(f"{lower} {equal} {greater}")
        lower = equal = greater = 0
    