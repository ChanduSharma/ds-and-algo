def bubble_sort(A):
    itr = 0
    for i in range(len(A)):
        for j in range(len(A) -i -1):
            itr += 1
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1],A[j]

    return A, itr

A = [9,8,7,6,5,4,3,2,1]

print(bubble_sort(A))