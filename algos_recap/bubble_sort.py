def bubble_sort(A):
    for i in range(len(A)):
        for j in range(len(A) -i -1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1],A[j]

    return A

A = [9,8,7,6,5,4,3,2,1]

print(bubble_sort(A))