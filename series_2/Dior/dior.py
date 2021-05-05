import sys
sys.setrecursionlimit(2500*1000)

from random import randint





def partition(array: list, p: int, r: int) -> int:
    
    x = array[r]
    i = p-1
    
    for j in range(p, r):
        if array[j] <= x:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i+1], array[r] = array[r], array[i+1]

    return i+1




def randomized_partition(array: list, p: int, r: int) -> int:

    i = randint(p, r)
    array[i], array[r] = array[r], array[i]

    return partition(array, p, r)





def randomized_quick_sort(array: list, p: int, r: int) -> None:

    if p < r:
        q = randomized_partition(array, p, r)
        randomized_quick_sort(array, p, q-1)
        randomized_quick_sort(array, q+1, r)









def solve(p: int, r: int) -> None:

    global count, places, pivots

    if r-p >= 1:
        count += r - p - 1
        q = places[pivots.pop(0)]
        solve(p, q)
        solve(q+1, r)

        




if __name__ == "__main__":

    n = int(input())
    arr = [int(num) for num in input().split()]
    pivots = [int(num) for num in input().split()]


    randomized_quick_sort(arr, 0, len(arr)-1)


    places = {}
    for i in range(n):
        places[arr[i]] = i
        

    count = 0
    solve(0, n)


    print(count)
