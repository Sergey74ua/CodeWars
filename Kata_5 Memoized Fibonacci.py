# Memoized Fibonacci

arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597,
  2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811,
  514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352,
  24157817, 39088169, 63245986, 102334155]
def fibonacci(n):
  while n >= len(arr):
      arr.append(arr[-1]+arr[-2])
  return(arr[n])


# тест для локального запуска
test = 70
print(test, "- входящая строка")
print(fibonacci(test), "- 190392490709135")
input()

# более короткий вариант
# def fibonacci(n, cache = [0, 1]):
#    if len(cache) <= n:
#        cache.append(fibonacci(n - 1) + fibonacci(n - 2))
#    return cache[n]