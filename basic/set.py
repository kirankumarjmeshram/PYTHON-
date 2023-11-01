s = {112,3,3,4,55,2,4,5,3,2,3,}
print(s) #{112, 2, 3, 4, 5, 55}

s.add(99)
s.add(89)
s.add(79)

print(s) #{2, 3, 4, 5, 79, 89, 99, 112, 55}

print(2 in s) #True

s2 = {2,2,3,5,4,6,43,22,4,5,222,66,99}

print(s.union(s2))  #{2, 3, 4, 5, 6, 66, 79, 22, 89, 222, 99, 43, 112, 55}
print(s.difference(s2)) #{112, 89, 55, 79}
print(s.intersection(s2)) #{2, 99, 3, 4, 5}