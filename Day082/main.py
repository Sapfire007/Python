# Multithreading in Python

import threading
import time

# Indicates some task being done
def func(seconds):
  print(f"Sleeping for {seconds} seconds")
  time.sleep(seconds)

# Normal Code
time1 = time.perf_counter()
func(7)
func(4)
func(1)
time2 = time.perf_counter()
print(time2-time1)

print("\n")
print("\n")

# Same code using threads
time3 = time.perf_counter()
t1 = threading.Thread(target=func,args=[7])
t2 = threading.Thread(target=func,args=[4])
t3 = threading.Thread(target=func,args=[1])
t1.start()
t2.start()
t3.start()

t1.join() # Wait till t1 is fully executed
t2.join() # Wait till t2 is fully executed
t3.join() # Wait till t3 is fully executed
time4 = time.perf_counter()
print(time4-time3)