"""
Check whether sum of two element equal k
"""

def check_sum(arr, target):

    i = 0
    j = len(arr) - 1

    while i < j:

        sum_of_element = arr[i] + arr[j]
        if sum_of_element == target:
            return True
        elif sum_of_element < target:
            i += 1
        else:
            j -= 1
    return False
    
A = [-2, 1, 2, 4, 7, 11]
target = 13

print(check_sum(A,target))