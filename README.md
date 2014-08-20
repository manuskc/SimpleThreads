SimpleThreads - A simple thread pool utility
============
A simple thread pool for python 2.x+<br/>
If you are missing ThreadPoolExecutor in python 2.x, here is a simple thread pool manager. 

Import:
============

       from simplethreads.ThreadPool import ThreadPool

Usage:
============

- Define tasks

        def task_a():
            # do something
            pass
            
        def task_b(a,b,c):
            # do something more
            pass
        
- Create a thread pool to schedule your tasks.
    
        from simplethreads.ThreadPool import ThreadPool

        # Create thread pool with nums threads
        pool = ThreadPool(nums)

		# Add a task into pool
        pool.process(task_a)

		# Pass arguments to task
        pool.process(task_b,1,2,3)

        # Cleanup before exit
		# default value of block=True
		# set to false if you dont want to wait till all the tasks are processed 
		# (Tasks will be processed in background though!)
        pool.shutdown(block=False) 
    
