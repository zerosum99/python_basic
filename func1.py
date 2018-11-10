
import time

n = 1000000

start_time = time.perf_counter()

results = 0
for i in range(n+1) :
    results += i**2

print(results)

end_time = time.perf_counter()

print(end_time - start_time)