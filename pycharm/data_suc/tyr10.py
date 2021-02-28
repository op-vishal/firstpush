import itertools

# List initialization 
list1 = [10,7,2,8,3]


# using itertools 
temp = list(itertools.product(list1, list1))


# output list initialization 
out = []

# iteration 
for elem in temp:
    if elem[0] != elem[1]:
        out.append(elem)

    # printing output
print(out) 