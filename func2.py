
import time

start_time = time.perf_counter()

def cel(n) :
    results = 0
    for i in range(n) :
         results += i**2

    print(results) 
    
cel(1000000)

end_time = time.perf_counter()

print(end_time - start_time)
