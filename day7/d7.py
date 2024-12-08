import sys

with open(sys.argv[1], 'r') as file:
	equations = []
	for line in file:
		parts = line.split(":")
		values = [int(num) for num in parts[1].split()]
		equations.append([int(parts[0])] + values)

def check_calibration(target: int, nums : list[int]) -> bool:
	if len(nums) == 2:
		return nums[1] + nums[0] == target or nums[0] * nums[1] == target
	if target - nums[-1] < nums[-2] and target % nums[-1]:
		return False
	return check_calibration(target - nums[-1], nums[:-1]) or check_calibration(target / nums[-1], nums[:-1])

def get_calibration_result() -> int:
	res = 0
	for equation in equations:
		if check_calibration(equation[0], equation[1:]):
			res += equation[0]
	return res

def check_calibration_new(target: int, nums : list[int]) -> bool:
	if len(nums) == 2:
		return nums[1] + nums[0] == target or nums[0] * nums[1] == target or nums[0] * pow(10, len(str(nums[1]))) + nums[1] == target
	if target - nums[-1] < nums[-2] and target % nums[-1] and (target - nums[-1]) % pow(10, len(str(nums[-1]))):
		return False
	return check_calibration_new(target - nums[-1], nums[:-1]) or check_calibration_new(target / nums[-1], nums[:-1]) or \
		check_calibration_new((target - nums[-1]) / pow(10, len(str(nums[-1]))), nums[:-1])

def get_calibration_result_new() -> int:
	res = 0
	for equation in equations:
		if check_calibration_new(equation[0], equation[1:]):
			print(equation)
			res += equation[0]
	return res

print("part 1: ", get_calibration_result())
print("part 2: ", get_calibration_result_new())
