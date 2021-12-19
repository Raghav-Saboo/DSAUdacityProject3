def sqrt(number):
  """
  Calculate the floored square root of a number

  Args:
     number(int): Number to find the floored squared root
  Returns:
     int: Floored Square Root
  """
  if number < 0:
    return None
  low = 0
  high = number
  ans = low
  while low <= high:
    mid = (low + high) // 2
    if mid * mid <= number:
      ans = mid
      low = mid + 1
    else:
      high = mid - 1
  return ans


# Test Case 1 Normal Case
print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")

# Test Case 2 Edge Case
print("Pass" if (98346 == sqrt(9671935716)) else "Fail")
print("Pass" if (None == sqrt(-1)) else "Fail")
