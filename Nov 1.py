class Solution():
  def fibonacci(self, n):
    fib = []
    for n in range (0,n):
        if n < 2:
            fib.append(1)
        else:
            fib.append(fib[n-1]+fib[n-2])
    return fib


n = 20
print(Solution().fibonacci(n))
# 34