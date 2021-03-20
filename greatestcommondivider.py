def greatest_common_divider(x, y):
    greatest_common_divider = 1
    if x % y == 0:
        return y   
    for k in range(int(y / 2), 0, -1):
        if x % k == 0 and y % k == 0:
            greatest_common_divider = k
            break  
    return greatest_common_divider
print(" gcd of 12 and 29 is ")
print(greatest_common_divider(12, 29))
print(" gcd of 91 and 132 is ")
print(greatest_common_divider(91, 132))
print(" gcd of 21 and 28 is ")
print(greatest_common_divider(21, 28))
