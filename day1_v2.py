elves = []
elf = []
with open("day1_input.txt", encoding = 'utf-8') as f:
	for line in f:
		if line == "\n":
			elves.append(sum(elf))
			elf = []
		else:
			elf.append(int(line.rstrip()))


print(max(elves))
print(sum(sorted(elves)[-3:]))
