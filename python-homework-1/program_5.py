# Explore with memory id()

a = 200
b = 200
print("a is b: ", a is b)
print("Memory ID of a:", id(a))
print("Memory ID of b:", id(b))


a = 2000
b = 2000
print("a is b: ", a is b)
print("Memory ID of a:", id(a))
print("Memory ID of b:", id(b))

# Both are giving me True result but, if there is an issue
# Small integers like 200 are cached by Python,
# while larger integers like 2000 are usually stored as separate objects.
