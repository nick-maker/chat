def readFile(fileName):
	lines = []
	with open(fileName, 'r') as f:
		for line in f:
			lines.append(line.strip().replace('\ufeff',''))
	return lines

def convert(lines):
	new = []
	person = None
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person:
			new.append(person + ': ' + line)
	return new

def writeFile(fileName, new):
	with open(fileName, 'w') as f:
		for line in new:
			f.write(line + '\n')

def main():
	lines = readFile('input.txt')
	new = convert(lines)
	writeFile('output.txt', new)

main()