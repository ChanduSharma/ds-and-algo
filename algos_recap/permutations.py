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

permute("ABC","")