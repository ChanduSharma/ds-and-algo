def bitonic_peak(arr):

    low = 0
    high = len(arr) - 1

    if len(arr) < 3:
        return None
    
    while low <= high:
        
        mid = (low + high) // 2

        if (mid == 0 or arr[mid-1] < arr[mid]) and (mid == len(arr) - 1 or arr[mid] > arr[mid+1]):
            return arr[mid]
    
        elif arr[mid] < arr[mid - 1]:
            high = mid - 1
            
        else:
            low = mid + 1
    
A = [1, 2, 3, 4, 5, 4, 3, 2, 1]
print(bitonic_peak(A))
A = [1, 6, 5, 4, 3, 2, 1]
print(bitonic_peak(A))
A = [1, 2, 3, 4, 5]
print(bitonic_peak(A))
A = [5, 4, 3, 2, 1]
print(bitonic_peak(A))