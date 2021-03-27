def test_distinct(data):
  if len(data) == len(set(data)):
    return True
  else:
    return False;
print(test_distinct([1,2,3,3,4,5,6,7,8,9]))
print(test_distinct([2,4,6,8,0,-2]))
