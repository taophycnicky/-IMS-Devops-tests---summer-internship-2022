#CPU METRICS

import psutil

psutil.cpu_times()



#MEM METRICS

import psutil

mem = psutil.virtual_memory()

print(mem)



import psutil

psutil.swap_memory()

