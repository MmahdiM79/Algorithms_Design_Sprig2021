









if __name__ == '__main__':

    n = int(input())

    i = 0
    while i < n:
        input()
        str1 = input()
        str2 = input()

        current_s1 = 0
        current_s2 = 0

        while current_s2 < len(str2):
            if current_s1 == len(str1):
                break

            if str2[current_s2] == str1[current_s1] and current_s1 < len(str1):
                current_s1 += 1

            current_s2 += 1

        if len(str1) == current_s1:
            print('YES')
        else:
            print('NO')

        i += 1
            


