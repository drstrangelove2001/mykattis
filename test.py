import random as rd
import time
lst = [rd.randint(0,10000) for _ in range(100000)]
start = time.time()
lst = sorted(lst, reverse=True)
print(time.time()-start)