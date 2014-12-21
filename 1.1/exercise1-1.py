# You have N-element tuple or sequence that you would like
# to unpack into a collection of N variables

t = ("a", "b", "mpilgrim", "z", "example")
# .split() wont work since tuples don't have attributes

a, b, c, d, e = t
# gotta match exactly or recieve "ValueError: too many values to unpack (expected 4)"

print (a)
print (b)
print (c)
print (d)
print (e)
