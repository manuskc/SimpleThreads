from Queue import Queue
from threading import Thread, Lock
import time

class _WorkerThread (Thread):
	def __init__(self, taskQueue):
		Thread.__init__(self)
		self.daemon = True
		self.shutdown_state = False
		self.taskQueue = taskQueue

	def shutdown(self):
		self.shutdown_state = True
	
	def run(self):
		while True:
			try:
				task = self.taskQueue.get(False)
				if(task is not None):
					task()
				else:
					time.sleep(1)
			except:
				pass

			if(self.shutdown_state): break

class ThreadPool:
	def __init__(self, num_threads):
		self.tasks = Queue(0) #infinite size
		self.threads = []
		self.shutdown_state = False
		self.lock = Lock()
		for _ in range(num_threads):
			self.threads.append(_WorkerThread(self.tasks))
		map(lambda thread : thread.start(), self.threads)

	def process(self, task):
		if not self.shutdown_state:
			self.tasks.put(task)
	
	def shutdown(self):
		self.lock.acquire()
		try:
			if not self.shutdown_state:
				self.shutdown_state = True
				while not self.tasks.empty():
					time.sleep(1)
				map(lambda thread : thread.shutdown(), self.threads)
				map(lambda thread : thread.join(), self.threads)	
		except:
			pass
		finally:
		 	self.lock.release()

