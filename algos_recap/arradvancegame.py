"""
Is it possible to advance from the start of the array to the 
last element given that the maximum you can advance from a position
is based on the value of the array at the index you are currently present on?
"""

def array_advance(arr):
    farthest_reached = 0
    i = 0
    max_len = len(arr) - 1

    while i <= farthest_reached and farthest_reached < max_len:
        farthest_reached = max(farthest_reached, arr[i]+i)
        i += 1
    
    return farthest_reached >= max_len

arr = [1,3,1,0,2,0,1]

print("Reachable",arr)
print(array_advance(arr))

arr = [3,2,0,0,2,0,1]
print("Not Reachable",arr)
print(array_advance(arr))