class MedianFinder:
	__max_len = 5 * 10 ** 5
	__rborder = 10 ** 5
	__lborder = -__rborder

	def __init__(self):
		self.__seq = []

	def add_num(self, num: int):
		if num > self.__rborder or num < self.__lborder or len(self.__seq) >= self.__max_len:
			return
		self.__seq.append(num)

	def find_median(self):
		self.__seq = sorted(self.__seq)
		if len(self.__seq) == 0:
			return 0
		mid = len(self.__seq) // 2
		return round((self.__seq[mid] + self.__seq[~mid]) / 2, 5)


if __name__ == "__main__":
	median_finder = MedianFinder()
	assert median_finder.find_median() == .0

	median_finder.add_num(1)
	median_finder.add_num(2)
	assert median_finder.find_median() == 1.5

	median_finder.add_num(3)
	assert median_finder.find_median() == 2
