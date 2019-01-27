
Followed example from the original link:
https://chriskiehl.com/article/parallelism-in-one-line

# for multi-processing, CPU heavy tasks, use
from multiprocessing import Pool

# for multi-threading, IO heavy tasks, use
from multiprocessing.dummy import Pool as ThreadPool

# default thread number is the number of cores on the running machine
pool = ThreadPool() 
pool = ThreadPool(4)