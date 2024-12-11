import sys

with open(sys.argv[1], 'r') as file:
	tmap : list[str] = [line.strip() for line in file]

h = len(tmap)
w = len(tmap[0])

for i in range(h):
	tmap[i] = [int(char) for char in tmap[i]]

def hiking_trails(i : int, j : int, num : int, highest: set) -> set:
	global scores
	if i < 0 or j < 0 or i >= h or j >= w or tmap[i][j] != num:
		return highest
	if num == 9:
		highest.add((i, j))
	hiking_trails(i, j + 1, num + 1, highest)
	hiking_trails(i, j - 1, num + 1, highest)
	hiking_trails(i - 1, j, num + 1, highest)
	hiking_trails(i + 1, j, num + 1, highest)
	return highest

def cal_score() -> int:
	res = 0
	for i in range(h):
		for j in range(w):
			if tmap[i][j] == 0:
				highest = set()
				highest = hiking_trails(i, j, 0, highest)
				res += len(highest)
	return res

def hiking_trails_2(i : int, j : int, num : int) -> int:
	global scores
	if i < 0 or j < 0 or i >= h or j >= w or tmap[i][j] != num:
		return 0
	if num == 9:
		return 1
	return hiking_trails_2(i, j + 1, num + 1) + \
			hiking_trails_2(i, j - 1, num + 1) + \
			hiking_trails_2(i - 1, j, num + 1) + \
			hiking_trails_2(i + 1, j, num + 1)

def cal_score_2() -> int:
	res = 0
	for i in range(h):
		for j in range(w):
			if tmap[i][j] == 0:
				res += hiking_trails_2(i, j, 0)
	return res

# print(expand_block())
# print("part 1: ", cal_score())
print("part 2: ", cal_score_2())

