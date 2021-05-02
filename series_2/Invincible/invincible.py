








if __name__ == "__main__":

    n, m, k = [int(num) for num in input().split(' ')]


    buckets = {}
    for i in range(m//k):
        buckets[i] = []


    for num in input().split():
        buckets[int(num)//k].append(int(num))


    

