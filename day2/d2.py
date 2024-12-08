import sys

with open(sys.argv[1], 'r') as file:
	lines : list[str] = file.readlines()


def get_diffs(lines : list[str]) -> list[list[int]]:
	level = []
	diffs = []
	for line in lines:
		level = [int(x) for x in line.split()]
		diff = []
		for i in range(len(level) - 1):
			diff.append(level[i] - level[i + 1])
		diffs.append(diff)
	return diffs

def check_safety(diff : list[int]) -> bool:
	flag = 1 if diff[0] > 0 else 0
	for num in diff:
		if flag == 1 and (num > 3 or num < 1) :
			return False
		if flag == 0 and (num < -3 or num > -1) :
			return False
	return True

# def check_tolerant_safety(diff : list[int]) -> bool:
	

def get_safety_count(diffs : list[list[int]]) -> int :
	count = 0
	for diff in diffs:
		if (check_safety(diff)) :
			count += 1			
	return count

	

print("part 1: ", get_safety_count(get_diffs(lines)))
# print("part 2: ", check_tolerant_safety(get_diffs(lines)))

