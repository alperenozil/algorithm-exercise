def is_group_member(group_data, n):
    for value in group_data:
        if n == value:
            return True
    return False
print(is_group_member([1, 5, 8, 3], 3))
print(is_group_member([0, 2, 4, 6, 8, 10, 12], 7))
print(is_group_member([5, 8, 3], -1))
