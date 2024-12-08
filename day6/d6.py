import sys

with open(sys.argv[1], 'r') as file:
	mymap : list[str] = file.readlines()


		

print("part 1: ", count_visit())
# for line in mymap:
# 	print(line)
# print("part 2: ", )

