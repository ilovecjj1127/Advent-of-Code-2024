import sys

with open(sys.argv[1], 'r') as file:
	letters : list[list[str]] = [list(line.strip()) for line in file]

xmas = "XMAS"

def check_xmas(letters : list[list[str]], i : int, j : int, di : int, dj : int) -> bool:
	for pos in [1, 2, 3]:
		newi = i + di * pos
		newj = j + dj * pos
		if (newi < 0 or newi >= len(letters) or newj < 0 or newj >= len(letters[0]) or letters[newi][newj] != xmas[pos]):
			return False
	return True

def count_surrounding_xmas(letters : list[list[str]], i : int, j : int) -> int:
	if (letters[i][j] != "X"):
		return 0
	count = 0
	for di in [-1, 0, 1]:
		for dj in [-1, 0, 1]:
			if not check_xmas(letters, i, j, di, dj):
				continue
			count += 1
	return count

def check_x_max(letters : list[list[str]], i : int, j : int, letter : str) -> bool:
	if (i < 0 or i >= len(letters) or j < 0 or j >= len(letters[0]) or letters[i][j] != letter):
		return False
	return True
	
def check_surrounding_x_mas(letters : list[list[str]], i : int, j : int) -> bool:
	if letters[i][j] != "A":
		return False
	if not (
		(check_x_max(letters, i - 1, j - 1, "M") and check_x_max(letters, i + 1, j + 1, "S"))
		or
		(check_x_max(letters, i - 1, j - 1, "S") and check_x_max(letters, i + 1, j + 1, "M"))
	):
		return False
	if not (
		(check_x_max(letters, i + 1, j - 1, "M") and check_x_max(letters, i - 1, j + 1, "S"))
		or
		(check_x_max(letters, i + 1, j - 1, "S") and check_x_max(letters, i - 1, j + 1, "M"))
	):
		return False
	return True

def count_xmas(letters : list[list[str]]) -> int:
	count = 0
	h = len(letters)
	w = len(letters[0])
	for i in range(h):
		for j in range(w):
			count += count_surrounding_xmas(letters, i, j)
	return count
	
def count_x_mas(letters : list[list[str]]) -> int:
	count = 0
	h = len(letters)
	w = len(letters[0])
	for i in range(h):
		for j in range(w):
			count += 1 if check_surrounding_x_mas(letters, i, j) else 0
	return count

# print("part 1: ", count_xmas(letters))
print("part 2: ", count_x_mas(letters))

