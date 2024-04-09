def sum(a):
  def inner_sum(b):
    return a + b
  return inner_sum


test = sum(1)
print(test(2))
