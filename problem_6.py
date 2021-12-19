def get_min_max(ints):
  """
  Return a tuple(min, max) out of list of unsorted integers.

  Args:
     ints(list): list of integers containing one or more integers
  """
  if len(ints) == 0:
    return None, None
  mn = ints[0]
  mx = ints[0]
  for val in ints:
    if mn > val:
      mn = val
    if mx < val:
      mx = val
  return mn, mx


## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
print("Pass" if ((200, 200) == get_min_max([200])) else "Fail")
print("Pass" if ((None, None) == get_min_max([])) else "Fail")
