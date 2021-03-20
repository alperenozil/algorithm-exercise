def sumofintegers(x, y, z):
    if x == y or y == z or x==z:
        sumofintegers = 0
    else:
        sumofintegers = x + y + z
    return sumofintegers

print(sumofintegers(1, 2, 3))
print(sumofintegers(5, 15, 25))
print(sumofintegers(2, 12, 42))
print(sumofintegers(11, 21, 321))
