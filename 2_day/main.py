import re
import sys

sys.path.append(".")
from engine import get_input


def one(data):
	suma = []
	for n, i in enumerate(data):
		true_list = [True]
		for i in [ i.replace(" ", "").split(",") for i in i.split(":")[1].split(";") ]:
			out = {"red": 0, "green":0, "blue": 0}
			for j in i:
				out["".join(re.findall(r"[a-z]", j))] += int(re.findall(r"\d+", j)[0])
			if not( out["red"] <= 12 and out["green"] <= 13 and out["blue"] <= 14):
				true_list.append(False)
		if all(true_list):
			suma.append(n+1)
	return sum(suma)

def two(data):
	suma = []
	for i in data:
		out = {"red": 0, "green":0, "blue": 0}
		for b in [ i.replace(" ", "").split(",") for i in i.split(":")[1].split(";") ]:
			for j in b:
				if out["".join(re.findall(r"[a-z]", j))] < int(re.findall(r"\d+", j)[0]):
					out["".join(re.findall(r"[a-z]", j))] = int(re.findall(r"\d+", j)[0])
		suma.append([s := 1, [s := s * num for num in out.values()]][-1][-1])
	return sum(suma)

if __name__ == "__main__":
	data = [i.strip("\n") for i in get_input("2")]
	print(one(data))
	print(two(data))