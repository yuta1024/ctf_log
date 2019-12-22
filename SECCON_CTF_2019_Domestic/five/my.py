#!/usr/bin/env python3

import math
import copy
import random
import pprint
import os
import subprocess

class AI:
	
	def __init__(self):
		self.DIRECTION = { "UP": 0, "DOWN": 1, "RIGHT": 2, "LEFT": 3 }
		self.route = []

	def move(self, _map, snakes, turn):
		with open('./input.txt' , 'w') as f:
			print("%d" % turn, file=f)
			print("%d %d" % (len(_map), len(_map[0])), file=f)
			for y in range(0, len(_map)):
				for x in range(0, len(_map[y])):
					print(_map[y][x], end=' ', file=f)
				print("", file=f)

			print("%d" % len(snakes[0]), file=f)
			for i in range(0, len(snakes[0])):
				_x, _y = snakes[0][i]
				print("%d %d" %(_x, _y), file=f)

			print("%d" % len(snakes[1]), file=f)
			for i in range(0, len(snakes[1])):
				_x, _y = snakes[1][i]
				print("%d %d" %(_x, _y), file=f)

		res = subprocess.check_output("./a.out").decode(encoding='utf-8')
		return int(res)

ai = AI()
def main(d):
	return ai.move(d["map"], d["snakes"], d["turn"])
