from datetime import datetime

class MyTimer:
	__available_units = ["s", "m", "h"]
	
	def __init__(self, units: str):
		if units not in self.__available_units:
			raise Exception("")
		self.__units = units

	def __enter__(self):
		self.__start_time = datetime.now()
		return self

	def __exit__(self, type, value, traceback):
		self.spent_time = datetime.now() - self.__start_time

	def elapsed_time(self):
		seconds = self.spent_time.total_seconds()
		if self.__units == "s":
				return seconds
		elif self.__units == "m":
				return seconds / 60.0
		elif self.__units == "h":
				return seconds / 3600.0 

if __name__ == "__main__":
	with MyTimer(units="s") as t:
		print("Hello world")

	print(t.elapsed_time())

