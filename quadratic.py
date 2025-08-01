import time

def linear_time(n):
    print(f"\nTesting for n={n}")
    start = time.time()
    for i in range(n):
        for j in range(n):
         pass
    end = time.time()
    print(f"Time taken: {end - start} seconds")

linear_time(100)
linear_time(200)
linear_time(300)
