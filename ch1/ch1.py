output = 0
for l in open('input.txt'):
	output += math.floor(l/3)-2
print(output)