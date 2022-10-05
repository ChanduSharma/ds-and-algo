def permute(initial_string, remaining_string):

    if not initial_string:
        print(remaining_string)
    else:
        for i in range(len(initial_string)):
            letter = initial_string[i]
            head = initial_string[0:i]
            tail = initial_string[i+1:]
            remaining = head + tail
            permute(remaining, letter + remaining_string)


def permute_swap(str, l, r):

    if l == r:
        print(''.join(str))
    else:
        for i in range(l, r+1):
            str[l], str[i] = str[i], str[l]
            permute_swap(str, l+1, r)
            str[l],str[i] = str[i], str[l]




permute_swap(['A','B', 'C'],0,2)