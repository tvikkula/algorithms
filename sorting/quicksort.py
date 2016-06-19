def quicksort(alist, left = 0, right = None):

    def partition(alist, first, last):
        pivot = alist[first]
        right = last
        left = first + 1

        while True:
            while left <= right and alist[left] <= pivot:
                left = left + 1
            while alist[right] >= pivot and right >= left:
                right = right - 1
            if right < left:
                break
            else:
                temp = alist[left]
                alist[left] = alist[right]
                alist[right] = temp

        temp = alist[first]
        alist[first] = alist[right]
        alist[right] = temp
        return right

    if right is None:
        right = len(alist) - 1

    if left < right:
        split = partition(alist, left, right)
        quicksort(alist, left, split - 1)
        quicksort(alist, split + 1, right)

    return alist
