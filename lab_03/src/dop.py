def insertion_sort(a):
    for i in range(len(a)):
        j = i - 1
        buff = int(a[i])
        while int(a[j]) > buff and j >= 0:
            a[j + 1] = int(a[j])
            j -= 1
        a[j + 1] = buff

    return a
