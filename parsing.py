import sys

import sys
import glob



def read_puzzle(filename):

	with open(filename) as f:
		content = f.readlines()

	content = content[3:]

	size = content[0]

	size = size.split()

	content = content[1:]

	m = []


	for i in range(int(size[0])):
		temp = []
		for j in range(int(size[1])):
			temp.append(0)
		m.append(temp)

	row = 0

	for line in content:
		col = 0
		x = line.split()

		line = "".join(x)

		for i in line:
			try:

			  x = int(i)

			except:

				i = i.encode('utf-8')
				x = i.hex()
				x = int(x)

			m[row][col] = x
			col += 1

		row +=1





	for i in m:
		print(i)
	return m




fileNames = glob.glob("puzzles/*.txt")


for fileName in fileNames:

	matrix = read_puzzle(fileName)

	






































