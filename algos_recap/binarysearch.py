def binary_search(arr, l, r, target):

    while l <= r:

        mid = (l+r) // 2

        if arr[mid] < target:
            l = mid + 1
        elif arr[mid] > target:
            r = mid - 1
        else:
            return mid
    
    return -1


def binary_search_rec(arr, l, r, target):

    if l <= r:

        mid = (l + r) // 2

        if arr[mid] < target:
            return binary_search_rec(arr, mid + 1, r, target)
        
        elif arr[mid] > target:
            return binary_search_rec(arr, l, mid - 1, target)
        
        else:
            return mid
    else:
        return -1


print(binary_search_rec([2,4,6,6,7,8,9], 0, 6, 9))