import sys

with open(sys.argv[1], 'r') as file:
	disk_map : str = file.readline().strip()

def expand_file() -> list:
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

def find_sublist(file : list, sublist : list) -> int:
	n, m = len(file), len(sublist)
	for i in range(n - m + 1):
		if file[i] == "." and file[i:i + m] == sublist:
			return i
	return -1

def move_file_blocks(file : list) -> list:
	label = sys.maxsize
	for i in range(len(file) - 1, -1, -1):

		if file[i] == ".":
			continue
		if int(file[i][0]) >= label:
			continue
		label = int(file[i][0])
		sz = len(file[i])
		id = find_sublist(file[:i], ["."] * sz)
		if id == -1:
			continue
		for j in range(id, id + sz):
			file[j] = file[i][0]
		file[i] = ["."] * sz
	return file

def flatten_list(filelist : list) -> list:
	flattened_list = []
	for sublist in filelist:
		if isinstance(sublist, list):
			for item in sublist:
				flattened_list.append(item)
		else:
			flattened_list.append(sublist)
	return flattened_list

def filesystem_checksum(filesystem : list) -> int:
	flattened_list = flatten_list(filesystem)
	res = 0
	for i, c in enumerate(flattened_list):
		if c == ".":
			continue
		res += i * int(c) 
	return res

# print(expand_file())
# print(move_file_blocks(expand_file()))
# print(flatten_list(move_file_blocks(expand_file())))
print("part 2: ", filesystem_checksum(move_file_blocks(expand_file())))
