def count_1s(nums):
  count = 0  
  for num in nums:
    if num == 1:
      count = count + 1

  return count

print(count_1s([1, 2, 3, 0, 9, 7, 1, 2, 3, 1]))
print(count_1s([1, 4, 6, 1]))