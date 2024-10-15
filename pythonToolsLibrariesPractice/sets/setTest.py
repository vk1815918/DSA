

l1 = [1,2,3,4,5]
l2 = [4,5,6,7,8,9]


# Union

## both work the same and give the same output
print("Union: ", set(l1).union(set(l2)))
print("Union: ", set(l1) | (set(l2)))


# Intersection
## both ways can be used to derive the intersection
print("Intersection: ", set(l1).intersection(set(l2)))
print("Intersection: ", set(l1) & (set(l2)))

if set(l1) & set(l2):
    print("There is intersection")
else:
    print("There is no intersection")

