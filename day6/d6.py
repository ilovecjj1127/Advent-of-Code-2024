import sys

with open(sys.argv[1], 'r') as file:
	mymap : list[str] = file.readlines()

for i in range(len(mymap)):
	if "^" in mymap[i]:
		pos = [i, mymap[i].find("^")]
	mymap[i] = list(mymap[i].strip())

h = len(mymap)
w = len(mymap[0])
di = [-1, 0, 1, 0] # -1 -> 0 -> 1 -> 0
dj = [0, 1, 0, -1] # 0 -> 1 -> 0 -> -1

def walking_guard(i : int, j : int, dir : int) -> None:
	while (i >= 0 and j >= 0 and i < h and j < w):
		mymap[i][j] = "X"
		newi = i + di[dir]
		newj = j + dj[dir]
		if (newi >= 0 and newj >= 0 and newi < h and newj < w and mymap[newi][newj] == "#"):
			dir = (dir + 1) % 4
		i = i + di[dir]
		j = j + dj[dir]

def count_visit() -> int:
	walking_guard(pos[0], pos[1], 0)
	res = 0
	for str in mymap:
		res += str.count("X")
	return res
		

print("part 1: ", count_visit())
# for line in mymap:
# 	print(line)
# print("part 2: ", )

