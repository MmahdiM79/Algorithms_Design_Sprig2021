

def substrfinder(s1, s2, n, m):

    dp = [[0 for x in range(m+1)] for x in range(n+1)]
	
    i = 0; j = 0;
    while i <= n:
        j = 0
        while j <= m:
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

            j += 1
        i += 1

    index = dp[n][m]

    lcs = [""] * (index+1)
    lcs[index] = ""

    i = n
    j = m
    while i > 0 and j > 0:

        if s1[i-1] == s2[j-1]:
            lcs[index-1] = s1[i-1]
            i-=1
            j-=1
            index-=1

        elif dp[i-1][j] > dp[i][j-1]:
            i-=1
        else:
            j-=1

    return "".join(lcs)






if __name__ == '__main__':

    m, n, x, y = (int(x) for x in input().split())
    s1 = input()
    s2 = input()


    res = substrfinder(s1, s2, m, n)
    if len(res) == 0:
        print((len(s1)*x) + (len(s2)*y))
        exit()


    cost = 0

    i = 0; j = 0;
    while i < len(s1):
        if s1[i] == res[j]:
            i += 1; j += 1
        else:
            cost += x
            i += 1

        if j >= len(res):
            break

    if i < len(s1):
        cost += (len(s1)-i) * x
        


    i = 0; j = 0;
    while i < len(s2):
        if s2[i] == res[j]:
            i += 1; j += 1
        else:
            cost += y
            i += 1

        if j >= len(res):
            break

    if i < len(s2):
        cost += (len(s2)-i) * y


    print(cost)





