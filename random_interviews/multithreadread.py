import sys
import os
import time
import threading


# def thread_print(*args,**kwargs):
# 	with s_print_lock:
# 		time.sleep(0.1)
# 		print(*args,**kwargs)

# class Writer(threading.Thread):
# 	"""
# 	A class to create writer threads for each files with
# 	which this object is created.
# 	"""
# 	def __init__(self, filename):
# 		super(Writer, self).__init__()
# 		self.filename = filename
# 		self.lineGen = (line for line in open(self.filename,'r'))

# 	def run(self):

# 		thread_print(next(self.lineGen))
class Loader(object):
		"""docstring for Loader"""
		def __init__(self, filenameList):
			super(Loader, self).__init__()
			self.fileList = filenameList
			self.s_print_lock = threading.Lock()
			self.filesGenerator = [self._line(filename) for filename in self.fileList]
			self.threads = []

		def _line(self, filename):
			"""
			File line generator based on the filename
			"""
			for line in open(filename,'r'):
				self.s_print(line)

		def s_print(self,*args):
			with self.s_print_lock:
				time.sleep(0.1)
				print(*args)

		def run_threads(self):
			for generators in self.filesGenerator:
				self.threads.append(threading.Thread(target=self.s_print,args = [generators]))
				self.threads[-1].start()

			for thread in self.threads:
				thread.join()


def main():

	if len(sys.argv) == 1:
		sys.exit(1)
	else:
		filenames = sys.argv[1:]

		obj = Loader(filenames)
		obj.run_threads()


if __name__ == '__main__':
	main()