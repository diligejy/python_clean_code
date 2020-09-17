a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print('First four:', a[:4])
print('Last four:', a[-4:])
print('Middle two:', a[3:-3])

b = a[4:]
print('Before : ', b)
b[1] = 99
print('After : ', b)
print('No change : ', a)

b = a[:]
assert b == a and b is not a

b = a
print('Before', a)
a[:] = [101, 102, 103]
assert a is b
print('After ', a)