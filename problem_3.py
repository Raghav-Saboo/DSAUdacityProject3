def merge(arr1, arr2):
  l1 = len(arr1)
  l2 = len(arr2)
  i1 = 0
  i2 = 0
  ans = []
  while i1 < l1 and i2 < l2:
    if arr1[i1] < arr2[i2]:
      ans.append(arr1[i1])
      i1 += 1
    else:
      ans.append(arr2[i2])
      i2 += 1
  ans += arr1[i1:]
  ans += arr2[i2:]
  return ans


def merge_sort(arr):
  l = len(arr)
  if l <= 1:
    return arr
  mid = l // 2
  left = arr[:mid]
  right = arr[mid:]
  la = merge_sort(left)
  ra = merge_sort(right)
  return merge(la, ra)


def rearrange_digits(input_list):
  """
  Rearrange Array Elements so as to form two number such that their sum is maximum.

  Args:
     input_list(list): Input List
  Returns:
     (int),(int): Two maximum sums
  """
  sorted_list = merge_sort(input_list)
  n1 = 0
  n2 = 0
  for i in range(len(sorted_list) - 1, -1, -1):
    if i % 2 == 0:
      n1 *= 10
      n1 += sorted_list[i]
    else:
      n2 *= 10
      n2 += sorted_list[i]
  return [n1, n2]


def test_function(test_case):
  output = rearrange_digits(test_case[0])
  solution = test_case[1]
  if sum(output) == sum(solution):
    print("Pass")
  else:
    print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
