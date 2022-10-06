# home4_1
#1_1
a1 = 1
a2 = 1
a3 = 1
print(a1 == a2)
print(a2 == a3)
print(a1 is a2)
print(a2 is a3)
#1_2
b1 = ['s']
b2 = ['s']
print(b1 == b2)
print(b1 is b2)
#1_3
c1 = list((a1,))
c2 = list((a2,))
c3 = list((a3,))
print(c1 == c2)
print(c2 == c3)
print(c1 is c2)
print(c2 is c3)

d1 = bool(b1)
d2 = bool(b1)
print(d1 == d2)
print(d1 is d2)
