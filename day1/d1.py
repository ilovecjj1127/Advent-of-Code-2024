import sys

with open(sys.argv[1], 'r') as file:
	lines : list[str] = file.readlines()

def get_number_lists(lines : list[str]) -> tuple[list[int], list[int]]:
	list1, list2 = [], []
	for line in lines:
		list1.append(int(line.split()[0]))
		list2.append(int(line.split()[1]))
	return list1, list2

def get_results(list1 : list[int], list2 : list[int]) -> int:
	list1.sort()
	list2.sort()
	return sum(abs(a - b) for a, b in zip(list1, list2))

def get_similarity(list1 : list[int], list2 : list[int]) -> int:
	list1.sort()
	res = 0
	for num in list1:
		res += list2.count(num) * num
	return res


list1, list2 = get_number_lists(lines)
print("part 1: ", get_results(list1, list2))
print("part 2: ", get_similarity(list1, list2))

