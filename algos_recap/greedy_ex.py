def assign_hole(mice, holes):
    if len(mice) != len(holes):
        return "Not same"

    mice.sort()
    holes.sort()

    max_diff = 0

    for i in range(len(mice)):
        if max_diff <  abs(mice[i] - holes[i]):
            max_diff = abs(mice[i] - holes[i])
    
    return max_diff

mice = [4,-4,2]
holes = [4,0,5]

min_time = assign_hole(mice, holes)

print("last mouse gets into the hole in time ", min_time)