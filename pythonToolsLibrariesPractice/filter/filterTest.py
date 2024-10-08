nums = [1,2,3,4,5,6,7,8,"hey",1.1,9,10, "hi", "test2", 1.1]

x = list(filter(lambda x: x if isinstance(x, (int,float)) else None, nums))

# x = lambda x, b: x**2 + f"this is the value of b: {b}"

# x = [y for y in nums if isinstance(y, (int,float, str))]

print(x)

