import os

import requests


def get_key():
	with open("session", "r") as o:
		key = o.read()
	return key

def get_input(day):
	with open(f"./{day}_day/input", "r") as o:
		data = o.readlines()
	return data

def input_graber(url, key):

	cookie = {
		"session" : key
	}
	r = requests.get(url, cookies=cookie)
	return r.text

def store_text(dir, text):
	with open(dir+"input", "w") as o:
		o.write(text)

if __name__ == "__main__":
	day = "4"
	url = f"https://adventofcode.com/2023/day/{day}/input"
	dir = f"./{day}_day/"
	if not os.path.exists(dir):
		os.makedirs(dir)
	key = get_key()
	text = input_graber(url, key)
	store_text(dir, text)