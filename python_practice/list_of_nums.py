def unique_elements(lists):
    x = []
    # for i in lists:
    #     if i not in x:
    #         x.append(i)
    # return x

    i = 0
    while i < len(lists):
        item = lists[i]
        if item not in x:
            x.append(item)
        i += 1
    return x

lists = [int(x) for x in input("Input:").split(",")]
u_e = unique_elements(lists)
print("Output", u_e)