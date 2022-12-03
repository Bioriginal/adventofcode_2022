# WIN: 6 pt, DRAW: 3 pt; LOSS: 0 pt
# A: ROCK 1pt , B: PAPER 2pt, C: SCISSOR 3pt
# X: LOSS, Y: DRAW, Z: WIN
scores = {'AA':4,'AB':8,'AC':3,'BA':1,'BB':5,'BC':9,'CA':7,'CB':2,'CC':6}
strategy = {'AX':'AC','AY':'AA','AZ':'AB','BX':'BA','BY':'BB','BZ':'BC','CX':'CB','CY':'CC','CZ':'CA'}
matches = []
with open("day2_input.txt", encoding = 'utf-8') as f:
	for line in f:
		matches.append(line.replace(" ","").rstrip())

total = 0
for match in matches:
	total += scores[strategy[match]]

print(total)