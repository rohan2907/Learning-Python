# Faltening the nested list

def flatten(L):
    for ele in L:
        if hasattr(ele, '__iter__') and not isinstance(ele, str):
            yield from flatten(ele)
        else:
            yield ele

L = [1,2,[3,4,[5,6]],7,[8,9]]
flat = list(flatten(L))
print(flat)
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
