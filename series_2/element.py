






if __name__ == "__main__":

    n = int(input())

    array = [int(x) for x in input().split()]
    array.sort()

    Max = max(array)
    Min = min(array)



    num_questions = int(input())


    lower_index = 0; equals = 0; greater_index = 0

    for _ in range(num_questions):

        curr = int(input())
        if curr < Min:
            print(f'0 0 {n}')
            continue
        if curr > Max:
            print(f'{n} 0 0')
            continue


        start, end = 0, len(array)-1
    
        while True:
        
            mid = (end + start)//2
            

            if array[mid] == curr:
                equals = 1
                lower_index = mid-1
                greater_index = mid+1
                

                for i in range(greater_index, n):
                    if array[i] != curr:
                        greater_index = i
                        break
                    else:
                        equals += 1

                
                for j in range(lower_index, -1, -1):
                    if array[j] != curr:
                        lower_index = j
                        break
                    else:
                        equals += 1

                break
                    

            
            if start == mid:
                break

            if curr < array[mid]:
                end = greater_index = mid
            else:
                start = lower_index = mid+1
                




        print(f"{lower_index + 1} {equals} {n - greater_index}")
        lower_index = equals = greater_index = 0
    