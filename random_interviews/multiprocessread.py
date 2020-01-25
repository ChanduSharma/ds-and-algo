import sys
import multiprocessing
import time

class Loader(object):
	"""docstring for Loader"""
	def __init__(self, filenames):
		super(Loader, self).__init__()
		self.fileList = filenames
		self.s_print_lock = multiprocessing.Lock()
		self.process = []
		
	def getLines(self,filename):
		
		with open(filename,'r') as f:
			for line in f:
				self.s_print(line)
	
	def s_print(self,*args,**kwargs):
		with self.s_print_lock:
			time.sleep(0.1)
			print(*args,**kwargs)


	def runProcesses(self):
		
		for filename in self.fileList:
			self.process.append(multiprocessing.Process(target=self.getLines, args=(filename,)))
			self.process[-1].start()

		for process in self.process:
			process.join()	


def main():
	if len(sys.argv) == 1:
		sys.exit(1)
	else:
		filenames = sys.argv[1:]

		obj = Loader(filenames)
		obj.runProcesses()


if __name__ == '__main__':
	main()
		