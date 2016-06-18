# 
# A divide-and-conquer algorithm for finding a count of inverses
# in O(nlogn)-time:
def invcount(array, length):
    if length == 1: return 0
    else:
        x = invcount(array[:length/2], length/2)
        y = invcount(array[length/2:], length/2)
        z = countsplits(x, y, length)
    return x + y + z
def countsplits(A, B, length):
    i = 0
    j = 0
    k = 0
    while k < length:
        if A[i] < B[j]:
            C[k] = A[i]
            i += 1
        elif B[j] < A[i]:
            C[k] = B[j]
            j += 1
        else:
            C[k] = A[i]
            k += 1
            C[k] = B[j]
            i += 1
            j += 1
        k += 1
arr = [1,3,2,4,6,5]
print(invcount(arr, 6))
