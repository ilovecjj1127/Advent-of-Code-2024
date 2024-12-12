import sys
from functools import lru_cache

with open(sys.argv[1], 'r') as file:
	stones : list[int] = [int(num) for num in file.readline().split()]


def blink(stones : list[int]) -> list[int]:
	new_stones = []
	for num in stones:
		if num == 0:
			new_stones.append(1)
		elif len(str(num)) % 2 == 0:
			sz = len(str(num)) // 2
			new_stones.append(int(str(num)[0:sz]))
			new_stones.append(int(str(num)[sz:]))
		else:
			new_stones.append(num * 2024)
	return new_stones

def multi_blink(stones : list[int], n : int) -> list[int]:
	for i in range(n):
		stones = blink(stones)
	return stones

print("part 1: ", len(multi_blink(stones, 25)))
print("part 2: ", len(multi_blink(stones, 75)))

