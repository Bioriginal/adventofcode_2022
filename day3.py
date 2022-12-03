import string

rucksacks = []
with open("day3_input.txt", encoding = 'utf-8') as f:
	for line in f:
		rucksacks.append(line.rstrip())

alphabet = string.ascii_lowercase + string.ascii_uppercase

total=0
for rucksack in rucksacks:
	length = len(rucksack)
	middle_index = length // 2
	first_bag = rucksack[:middle_index]
	second_bag = rucksack[middle_index:]
	similar_value = list(set(first_bag).intersection(set(second_bag)))[0]
	position = alphabet.index(similar_value) + 1
	total += position
	print("Intersection of {} and {} is {} position is {}".format(first_bag,second_bag,similar_value,position))


print(total)