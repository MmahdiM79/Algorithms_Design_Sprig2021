import sys
sys.setrecursionlimit(2500*1000)






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


    arr.sort()


    places = {}
    for i in range(n):
        places[arr[i]] = i
        

    count = 0
    solve(0, n)


    print(count)
