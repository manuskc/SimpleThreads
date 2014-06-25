Thread pool
============
A simple thread pool for python 2.x+
If you are missing ThreadPoolExecutor in python 2.x, here is a simple thread pool manager. 

Import:
============

       from ThreadPool import ThreadPool

Usage:
============

- Define tasks


        def task_a():
            # do something
            pass
            
        def task_b():
            # do something more
            pass
        
- Create a thread pool to schedule your tasks.
    
        from ThreadPool import ThreadPool
        # Create thread pool with nums threads
        pool = ThreadPool(nums)
        # Add a task into pool
        pool.process(task_a)
        pool.process(task_b)
        # Cleanup before exit
        pool.shutdown()
    
