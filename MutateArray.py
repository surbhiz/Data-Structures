def mutateTheArray(n, a):
    sum = 0
    b = []
    j = 1
    for i in range(n):
        if n == 1:
            return a
        if i == (n-1):
            sum = a[n-2]+a[n-1]+0
            b.append(sum)
        if j < n:
            if i == 0:
                sum = 0+a[i]+a[j]
                b.append(sum)
                j += 1

            else:
                sum = a[i-1]+a[i]+a[j]
                b.append(sum)

                j += 1
    return b


print(mutateTheArray(5, [4, 0, 1, -2, 3]))
