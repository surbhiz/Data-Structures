def duplicatesOnSegment(arr):
    total = 0
    for i in range(0, len(arr)):
        unique = 0
        test = {}
        for j in range(i, len(arr)):
            k = arr[j]
            if k not in test:
                test[k] = 1
            else:
                test[k] += 1

            if test[k] == 1:
                unique += 1
            elif test[k] == 2:
                unique -= 1
            if unique == 0:
                total += 1
    return total


print(duplicatesOnSegment([0, 0, 0]))
