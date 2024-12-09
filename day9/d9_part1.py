import sys

with open(sys.argv[1], 'r') as file:
	disk_map : str = file.readline().strip()

def expand_block() -> list[str]:
	file = []
	id = 0
	for i, c in enumerate(disk_map):
		sz = int(c)
		if i % 2 == 0:
			file += [str(id)] * sz
			id += 1
		else:
			file += ["."] * sz
	return file

def expand_file() -> list[str]:
	file = []
	id = 0
	for i, c in enumerate(disk_map):
		sz = int(c)
		if i % 2 == 0:
			file += [[str(id)] * sz]
			id += 1
		else:
			file += ["."] * sz
	return file

def move_file_blocks(file : list[str]) -> list[str]:
	for i in range(len(file) - 1, -1, -1):
		if file[i] == ".":
			continue
		id = file.index(".")
		if id > i:
			break
		file[id], file[i] = file[i], "."
	return file

def filesystem_checksum(filesystem : list[str]) -> int:
	res = 0
	for i, c in enumerate(filesystem):
		if c == ".":
			break
		res += i * int(c)
	return res

# print(expand_block())
print("part 1: ", filesystem_checksum(move_file_blocks(list(expand_block()))))
