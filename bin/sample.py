from simplethreads.ThreadPool import ThreadPool


def task_a():
  #do something
  pass
  
  
def task_b(n):
  for i in range(n):
    #do something
    pass
    

pool = ThreadPool(10)


for _ in range(100) :
  pool.process(task_a)
  

for n in range(100): 
  pool.process(lambda : task_b(n))
  
  
# Cleanup before exit , blocking call
pool.shutdown()
