import glob

import watchdog.events
import watchdog.observers
import time
import shutil
import os


class Handler(watchdog.events.PatternMatchingEventHandler):

	def on_created(self, event):
		print("Watchdog received created event - % s." % event.src_path)

		for i in os.listdir(src_path):
			name, extension = os.path.splitext(i)
			print(extension)
			if extension == ".txt":
				shutil.move(src_path+i, dst_path+i)
			elif extension == ".jpg":
				shutil.move(src_path + i, jpg_path + i)
			elif extension == ".pdf":
				shutil.move(src_path+i, pdf_path+i)

		# Event is created, you can process it now

	def on_modified(self, event):

		print("Watchdog received modified event - % s." % event.src_path)
	# Event is modified, you can process it now

if __name__ == "__main__":
	
	src_path = r"C:\Users\siphesihleg\OneDrive - ATNS\Documents\Movee\Pictures\\"
	dst_path = r"C:\Users\siphesihleg\OneDrive - ATNS\Documents\Movee\Practise\\"
	pdf_path = r"C:\Users\siphesihleg\OneDrive - ATNS\Documents\Movee\pdf\\"
	jpg_path = r"C:\Users\siphesihleg\OneDrive - ATNS\Documents\Movee\jpg\\"



	pattern = "*.txt"
	files = glob.glob(src_path+pattern)

	event_handler = Handler()
	observer = watchdog.observers.Observer()
	observer.schedule(event_handler, path=src_path, recursive=True)
	observer.start()
	try:
		while True:
			time.sleep(1)
	except KeyboardInterrupt:
		observer.stop()
	observer.join()
