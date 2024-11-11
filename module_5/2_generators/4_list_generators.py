#list vs gene

#memory usage, time 

import time


t1 =time.time()
l = ( i ** 2 for i in range(10000))
t2 = time.time()
print(time.time() - t2) #0.0006155967712402344

