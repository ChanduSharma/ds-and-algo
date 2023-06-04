def next_number(s):

    result = []
    i = 0
    while i < len(s): 
        count = 1
        while i < len(s) - 1 and s[i] == s[i+1]:
            count += 1
            i += 1
        result.append(str(count)+s[i])
        i += 1
    return "".join(result)


s = "1"
print(s)
for i in range(7):
    s = next_number(s)
    print(s)