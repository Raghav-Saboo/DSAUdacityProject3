def find_pivot_index(arr):
  low = 0
  high = len(arr) - 1
  pi = low
  while low <= high:
    mid = (low + high) // 2
    if arr[mid] > arr[0]:
      low = mid + 1
    else:
      pi = mid
      high = mid - 1
  return pi


def binary_search(arr, low, high, val):
  while low <= high:
    mid = (low + high) // 2
    if arr[mid] > val:
      high = mid - 1
    elif arr[mid] < val:
      low = mid + 1
    else:
      return mid
  return -1


def rotated_array_search(input_list, number):
  """
  Find the index by searching in a rotated sorted array

  Args:
     input_list(array), number(int): Input array to search and the target
  Returns:
     int: Index or -1
  """
  pi = find_pivot_index(input_list)
  ind = binary_search(input_list, 0, pi - 1, number)
  if ind != -1:
    return ind
  return binary_search(input_list, pi, len(input_list) - 1, number)


def linear_search(input_list, number):
  for index, element in enumerate(input_list):
    if element == number:
      return index
  return -1


def test_function(test_case):
  input_list = test_case[0]
  number = test_case[1]
  if linear_search(input_list, number) == rotated_array_search(input_list,
                                                               number):
    print("Pass")
  else:
    print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
