def quicksort(alist, right = None, left = 0):

    def partition(alist, left, right):
        pivot = alist[right]
        right = right - 1
        print alist, left, right, pivot

        while True:
            print right, left
            while left <= right and alist[left] <= pivot:
                print 'hi1'
                left = left + 1
            while alist[right] >= pivot and right >= left:
                print right, left, pivot, alist[right]
                print 'hi2'
                right = right - 1
            if right < left:
                print 'hi'
                break
            else:
                print 'doing'
                temp = alist[left]
                alist[left] = alist[right]
                alist[right] = temp

        print right
        return right

    if right is None:
        right = len(alist) - 1

    if left < right:
        split = partition(alist, left, right)
        quicksort(alist, left, split - 1)
        quicksort(alist, split + 1, right)

    return alist
