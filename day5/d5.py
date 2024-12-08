import sys

with open(sys.argv[1], 'r') as file:
	order_rules = {}
	all_updates = []
	flag = 1
	for line in file:
		if line == "\n":
			flag = 0
		elif flag == 1:
			key, value = map(int, line.split("|"))
			if key not in order_rules:
				order_rules[key] = []
			order_rules[key].append(value)
		else:
			all_updates.append([int(num) for num in line.split(",")])

correct_updates = []
incorrect_updates = []

def check_correct_order(rules : dict[int, list[int]], update : list[int]) -> bool:
	value = update[0]
	for key in update[1:]:
		if key in rules and value in rules[key]:
			return False
	return True
	

def get_correct_order(rules : dict[int, list[int]], updates : list[list[int]]) -> None:
	for update in updates:
		for i in range(len(update)):
			if i == len(update) - 1:
				correct_updates.append(update)
			elif not check_correct_order(rules, update[i:]):
				incorrect_updates.append(update)
				break

def check_position(rules : dict[int, list[int]], num : int, target : int) -> bool:
	return False


def fix_incorrect(updates : list[list[int]]) -> list[list[int]]:
	res_list = []
	for update in updates:
		res = [update[0]]
		for num in update[1:]:
			for j in range(len(res) - 1, -1, -1):
				if check_position(num, res[j]):
					res.index(j + 1, num)
		res_list.append(res)


def add_middle_num(my_updates : list[list[int]]) -> int:
	res = 0
	for update in my_updates:
		res += update[int(len(update) / 2)]
	return res			

get_correct_order(order_rules, all_updates)

print("part 1: ", add_middle_num(correct_updates))
print("part 2: ", add_middle_num(fix_incorrect(incorrect_updates)))

