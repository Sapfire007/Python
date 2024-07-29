import time

def calculate_sum(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Start the stopwatch
start_time = time.perf_counter()

# Calculate the sum of the first 1,000,000 positive integers
result = calculate_sum(1000000)

# Stop the stopwatch
end_time = time.perf_counter()

# Calculate elapsed time
elapsed_time = end_time - start_time

print(f"Sum: {result}")
print(f"Elapsed time: {elapsed_time:.6f} seconds")