








if __name__ == "__main__":

    n, m, k = [int(num) for num in input().split(' ')]


    buckets = {}
    for i in range(m//k):
        buckets[i] = []


    for num in input().split():
        buckets[int(num)//k].append(int(num))


    largest_bucket = (-1, [])
    for bucket in buckets.items():
        if len(bucket[1]) > len(largest_bucket[1]):
            largest_bucket = bucket


    print(largest_bucket[1][0])
    

