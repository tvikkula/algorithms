def mergesort(alist):
    if len(alist) <= 1:
        return alist

    mid = len(alist) / 2
    left = mergesort(alist[:mid])
    right = mergesort(alist[mid:])

    i, j, k = 0, 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            alist[k] = left[i]
            i += 1; k += 1
        else:
            alist[k] = right[j]
            j += 1; k += 1

    alist[k:] = left[i:] + right[j:]

    return alist
    
