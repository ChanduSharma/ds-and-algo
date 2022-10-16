def fractional_knapsack(value, weight, capacity):

    items = list(range(len(value)))

    ratio = [v // w for v, w in zip(value, weight)]

    srt_ratios = sorted(ratio, reverse=True)

    items.sort(key=lambda i: ratio[i], reverse=True)

    max_value = 0

    fractions = [0] * len(value)

    for i in items:
        if weight[i] <= capacity:

            fractions[i] = 1
            max_value += value[i]
            capacity -= weight[i]
        else:
            fractions[i] = capacity // weight[i]
            max_value += value[i] * capacity // weight[i]

    return max_value


weight = [30, 50, 10, 70, 40]

value = [150, 100, 90, 140, 120]
capacity = 150

print(fractional_knapsack(value, weight, capacity))
