






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


        start, end = 0, n-1
        mid = (start + end)//2
    
        while True:


            if start == mid:

                if n == 1:
                    lower_index = -1
                    equals = 1 if array[0] == curr else 0
                    greater_index = n
                    break

                if n == 2:
                    for i in range(n):
                        lower_index += 1 if curr < array[i] else 0
                        equals += 1 if curr == array[i] else 0
                        greater_index += 1 if curr > array[i] else 0
                    
                    lower_index -= 1
                    greater_index += n
                    break


                greater_index = n - greater_index
                break

            
            mid = (start + end)//2


            if array[mid] == curr:
                lower_index = mid-1
                equals = 1
                greater_index = mid+1
                

                for i in range(greater_index, n):
                    if array[i] != curr:
                        greater_index = i
                        break
                    else:
                        equals += 1
                else:
                    greater_index = i


                
                for j in range(lower_index, -1, -1):
                    if array[j] != curr:
                        lower_index = j
                        break
                    else:
                        equals += 1
                else:
                    lower_index = j

                break
                    

            

            if curr < array[mid]:
                end = mid
                greater_index = mid
            else:
                start = mid+1
                lower_index = mid+1
                




        print(f"{lower_index + 1} {equals} {n - greater_index}")
        lower_index = equals = greater_index = 0
    