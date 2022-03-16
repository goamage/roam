# tupple
items = (1, 2)

print(items)

# unpacking
a, b = (1, 2)

print(a)
print(b)


# unpacking and not using second variable
a, _ = (1, 2)

print(a)


# unpacking and grouping
a, b, *c = (1, 2, 3, 4, 5)
#a, b, *_ = (1, 2, 3, 4, 5)

print(a)
print(b)
print(c)


a, b, *c, d = (1, 2, 3, 4, 5)


print(a)
print(b)
print(c)
print(d)