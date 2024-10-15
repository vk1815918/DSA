from collections import defaultdict

# defaultdict is a subclass of dict that returns a default value when a key is not found.

# dd = defaultdict(lambda: "nope")


dd = defaultdict(list)

dd['a'].append(2)
dd['a'].append(3)   
dd['b'].append(4)
print(list(dd.items()))

dd2 = defaultdict(lambda: None)

dd2['i']=2

print(dd2['i'])
print(dd2['j'])


