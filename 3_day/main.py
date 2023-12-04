import re
import sys

sys.path.append(".")
from engine import get_input


def one(lines_data):
	suma = []
	for line_num, line in enumerate(lines_data):
		numbers = [ (match.group(), match.start()) for match in re.finditer(r"\d+", line)]
		for k, v in numbers:
			search_area = [(line_num, v-1), (line_num, v+ len(k))]
			for i in range(-1, len(k) + 1):
				search_area.extend([(line_num-1,v + i), (line_num+1,v + i)])
			for x,y in search_area:
				if x >= 0 and y >= 0 and x < len(lines_data)-1 and y < len(line)-1 and lines_data[x][y] != ".":
						suma.append(int(k))
						break
	return sum(suma)


def two(lines_data):
	suma = []
	for line_num, line in enumerate(lines_data):
		numbers = [ (match.group(), match.start()) for match in re.finditer(r"[*]", line)]
		for k, v in numbers:
			search_area = [(line_num, v-1), (line_num, v + 1), (line_num-1, v-1),(line_num-1, v), (line_num-1, v+1), (line_num+1, v-1),(line_num+1, v), (line_num+1, v+1)]
			nums = []
			for x,y in search_area:
				if x >= 0 and y >= 0 and x < len(lines_data) and y < len(line) and lines_data[x][y].isnumeric():
					for match in re.finditer(r"\d+", lines_data[x]):
						if match.start() <= y and match.end() >= y and int(match.group()) not in nums:
							nums.append(int(match.group()))
			if len(nums) == 2:
				suma.append(nums[0] * nums[1])
	return sum(suma)


if __name__ == "__main__":
	data = get_input("3")
	print(one(data))
	print(two(data))
