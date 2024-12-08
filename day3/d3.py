import sys
import re

with open(sys.argv[1], 'r') as file:
	content : str = file.read()


def get_muls(content : str) -> list[str]:
	pattern = r'mul\(\d+,\d+\)'
	mul_list = re.findall(pattern, content)
	return mul_list

def get_updated_muls(content : str) -> list[str]:
	pattern = r'mul\(\d+,\d+\)'
	start_mul = 0
	dont_list = re.finditer("don't()", content)
	do_list = re.finditer("do()", content)
	donts = [dont.start() for dont in dont_list]
	dos = [do.start() for do in do_list]
	mul = re.search(pattern, content[start_mul:])
	while mul:
		i = mul.start()
		

def cal_mul(muls : list[str]) -> int:
	sum = 0
	for mul in muls:
		pos1 = mul.find(",")
		pos2 = mul.find(")")
		num1 = int(mul[4:pos1])
		num2 = int(mul[pos1 + 1:pos2])
		sum += num1 * num2
	return sum
		

	

print("part 1: ", cal_mul(get_muls(content)))
# print("part 2: ", check_tolerant_safety(get_diffs(lines)))

