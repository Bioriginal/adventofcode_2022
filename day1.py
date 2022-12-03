elfs = []
elf = []
with open("day1_input.txt", encoding = 'utf-8') as f:
	for line in f:
		if line == "\n":
			elfs.append(elf)
			elf = []
		else:
			elf.append(int(line.rstrip()))

elvesCalories = []
for elf in elfs:
	sumCalories = 0	
	for calorie in elf:
		sumCalories += calorie
	elvesCalories.append(sumCalories)


def find_max(elvesCalories):
	maxCalories = 0
	elfWithMaxCalories = 1
	elfNumber = 1
	for cal in elvesCalories:
		if maxCalories < cal:
			maxCalories = cal
			elfWithMaxCalories = elfNumber
		elfNumber+=1
	return [elfWithMaxCalories,maxCalories]


elfWithMaxCal = find_max(elvesCalories)
print("The elf n°{} with {} has the max calories ! ".format(elfWithMaxCal[0],elfWithMaxCal[1]))

i = 1
totalCalories = 0
while i < 4:
	maxCal = find_max(elvesCalories)
	print("The elf n°{} with {} has the max calories ! ".format(maxCal[0],maxCal[1]))
	totalCalories += maxCal[1]
	elvesCalories.remove(maxCal[1])
	i+=1

print("Total Calories of {} for the 3 first elves".format(totalCalories))
