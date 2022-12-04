
camp = []
with open("day4_input.txt", encoding = 'utf-8') as f:
	for line in f:
		camp.append(line.rstrip())

totalContained = 0
for sections in camp:
    elfSections = sections.split(',')
    elfRange1 = [int(x) for x in elfSections[0].split('-')]
    elfRange2 = [int(x) for x in elfSections[1].split('-')]
    check =  (elfRange1[0] >= elfRange2[0] and elfRange1[1] <= elfRange2[1] ) or (elfRange2[0] >= elfRange1[0] and elfRange2[1] <= elfRange1[1])

    if check is True:
        print("{} or {} is fully contained".format(elfRange1,elfRange2))
        totalContained+=1

print(totalContained)


