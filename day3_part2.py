import string

rucksacks = []
with open("day3_input.txt", encoding = 'utf-8') as f:
	for line in f:
		rucksacks.append(line.rstrip())

#https://www.geeksforgeeks.org/break-list-chunks-size-n-python/?ref=lbp
rucksacksByGroup = [rucksacks[i:i + 3] for i in range(0, len(rucksacks), 3)]
alphabet = string.ascii_lowercase + string.ascii_uppercase
total=0
i=0

for group in rucksacksByGroup:
	similar_value = list(set(group[0]).intersection(set(group[1])).intersection(set(group[2])))[0]
	position = alphabet.index(similar_value) + 1
	total += position
	print("Intersection of {} and {} and {} is {} position is {}".format(group[0],group[1],group[2],similar_value,position))

print(total)


