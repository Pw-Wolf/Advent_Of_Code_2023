import re
import sys

sys.path.append(".")
from engine import get_input


def one(data):
	return sum([ int(re.findall(r'\d', i)[0] + re.findall(r'\d', i)[-1]) for i in data])


def two(data):
	dict_nums = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9', '1':'1', '2':'2', '3':'3', '4':'4', '5':'5', '6':'6', '7':'7', '8':'8', '9':'9'}
	rez = 0
	for i in data:
		nums = {ind:v for k, v in dict_nums.items() if (ind := i.find(k)) != -1}
		nums.update({ind:v for k, v in dict_nums.items() if (ind := i.rfind(k)) != -1})
		rez += int(nums[sorted(nums)[0]]+nums[sorted(nums)[-1]])
	return rez


if __name__ == "__main__":
	data = get_input("1")
	print(one(data))
	print(two(data))