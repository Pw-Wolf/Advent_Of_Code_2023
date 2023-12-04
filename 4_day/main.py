import sys
from collections import defaultdict

sys.path.append(".")
from engine import get_input


def one(raw_data):
	suma = []
	for i in raw_data:
		i = i.split(":")[1].strip("\n").split("|")
		suma.append(int(2 ** (len([ n for n in i[0].split() if n in i[1].split()]) - 1)))
	return sum(suma)

def two(raw_data):
	suma = defaultdict(int)
	for i, line in enumerate(raw_data):
		line = line.split(":")[1].strip("\n").split("|")
		suma[i] += 1
		for j in range(i + 1, i + 1 + sum([1 for w in line[0].split() if w in line[1].split()])):
			suma[j] += suma[i]
	return sum(suma.values())


if __name__ == "__main__":
	data = get_input("4")
	print(one(data))
	print(two(data))