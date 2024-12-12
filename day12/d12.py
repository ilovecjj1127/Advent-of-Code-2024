import sys

with open(sys.argv[1], 'r') as file:
	stones : list[str] = [line.strip() for line in file]

visited = [[0] * len(stones[0]) for _ in range(len(stones))]
gardens = [0, 0] # [perimeter, area]

def dfs(i: int, j: int, value: str):
	if i >= 0 and j >= 0 and i < len(stones) and j < len(stones[0]) and visited[i][j] == 1 and stones[i][j] == value:
		return
	if i < 0 or j < 0 or i >= len(stones) or j >= len(stones[0]) or stones[i][j] != value:
		gardens[0] += 1
		return
	visited[i][j] = 1
	gardens[1] += 1
	dfs(i + 1, j, value)
	dfs(i, j + 1, value)
	dfs(i - 1, j, value)
	dfs(i, j - 1, value)


def get_price() -> int:
	price = 0
	for i in range(len(stones)):
		for j in range(len(stones[0])):
			if visited[i][j] == 0:
				print(stones[i][j], ": ")
				gardens[0] = 0
				gardens[1] = 0
				dfs(i, j, stones[i][j])
				print(gardens)
				price += gardens[0] * gardens[1]
	return price


print("part 1: ", get_price())
# print("part 1: ", len(multi_blink(stones, 75)))

