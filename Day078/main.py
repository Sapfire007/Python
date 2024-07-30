# Function Caching in Python

from functools import lru_cache
import time

@lru_cache(maxsize=None)
def fn(x):
  time.sleep(5)
  return x*5

print(fn(20))
print("Done for fn(20)")
print(fn(2))
print("Done for fn(2)")
print(fn(7))
print("Done for fn(7)")

# The same code below gets executed instantly because it has been memoized in the cache memory

print(fn(20))
print("Done for fn(20)")
print(fn(2))
print("Done for fn(2)")
print(fn(7))
print("Done for fn(7)")

#The next code below wont be executed instantly because this has not been memoized

print(fn(17)) 
print("Done for fn(17)")