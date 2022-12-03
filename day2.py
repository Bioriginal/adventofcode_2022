# WIN: 6 pt, DRAW: 3 pt; LOSS: 0 pt
# A: ROCK 1pt , B: PAPER 2pt, C: SCISSOR 3pt
# X: ROCK 1pt , Y: PAPER 2pt, Z: SCISSOR 3pt
scores = {'AX': 4,'AY': 8,'AZ': 3, 'BX': 1,'BY': 5,'BZ': 9,'CX': 7,'CY': 2,'CZ': 6}
matches = []
with open("day2_input.txt", encoding = 'utf-8') as f:
	for line in f:
		matches.append(line.replace(" ","").rstrip())

total = 0
for match in matches:
	total += scores[match]

print(total)


