
camp = []
with open("day4_input.txt", encoding = 'utf-8') as f:
	for line in f:
		camp.append(line.rstrip())

total = 0
for sections in camp:
    elfSections = sections.split(',')
    elfRange1 = [int(x) for x in elfSections[0].split('-')]
    elfRange2 = [int(x) for x in elfSections[1].split('-')]

    if elfRange1[0] == elfRange1[1]:
        elf1List = [elfRange1[0]]
    else:
        elf1List = [x for x in range(elfRange1[0],elfRange1[1]+1)]

    if elfRange2[0] == elfRange2[1]:
        elf2List = [elfRange2[0]]
    else:
        elf2List = [x for x in range(elfRange2[0],elfRange2[1]+1)]

    #https://techbeamers.com/program-python-list-contains-elements/
    check =  any(item in elf1List for item in elf2List) or any(item in elf2List for item in elf1List)
    if check is True:
        #print("{} or {}  overlap".format(elfRange1,elfRange2))
        total+=1

print(total)



