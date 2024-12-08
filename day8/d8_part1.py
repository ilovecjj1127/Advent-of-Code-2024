import sys

with open(sys.argv[1], 'r') as file:
	mymap : list[str] = [list(line.strip()) for line in file]

antinodes = mymap.copy()
antennas = {}

for i in range(len(mymap)):
	for j in range(len(mymap[0])):
		if mymap[i][j] == ".":
			continue
		if mymap[i][j] not in antennas:
			antennas[mymap[i][j]] = []
		antennas[mymap[i][j]].append((i, j))

def update_antinodes(pos1 : tuple, pos2 : tuple) -> None:
	h, w = len(mymap), len(mymap[0])
	at1 = (2 * pos1[0] - pos2[0], 2 * pos1[1] - pos2[1])
	at2 = (2 * pos2[0] - pos1[0], 2 * pos2[1] - pos1[1])
	if at1[0] >= 0 and at1[0] < h and at1[1] >= 0 and at1[1] < w:
		antinodes[at1[0]][at1[1]] = " "
	if at2[0] >= 0 and at2[0] < h and at2[1] >= 0 and at2[1] < w:
		antinodes[at2[0]][at2[1]] = " "

for value in antennas.values():
	sz = len(value)
	for i in range(sz - 1):
		for j in range(i + 1, sz):
			update_antinodes(value[i], value[j])
	
def count_antinode_locations() -> int:
	res = 0
	for line in antinodes:
		res += line.count(" ")
	return res

print("part 1: ", count_antinode_locations())

# print("part 2: ", get_calibration_result_new())
