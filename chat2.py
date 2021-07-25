def readFile(fileName):
	lines = []
	with open(fileName, 'r') as f:
		for line in f:
			lines.append(line.strip().replace('\ufeff',''))
	return lines


def split(lines):
	allenWordCounts = 0
	vikiWordCounts = 0
	allenStickerCount = 0
	vikiStickerCount = 0
	allenPictureCount = 0
	vikiPictureCount = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allenStickerCount += 1
			elif s[2] == '圖片':
				allenPictureCount += 1
			else:
				for m in s[2:]:
					allenWordCounts += len(m)
		elif name == 'Viki':
			if s[2] == '貼圖':
				vikiStickerCount += 1
			elif s[2] == '圖片':
				vikiPictureCount += 1
			else:
				for m in s[2:]:
					vikiWordCounts += len(m)
	print('Allen said', allenWordCounts, 'words, sent', allenStickerCount, 'stickers and sent', allenPictureCount, 'pictures.')
	print('Viki said', vikiWordCounts, 'words, sent', vikiStickerCount, 'stickers and sent', vikiPictureCount, 'pictures.')


def writeFile(fileName, new):
	with open(fileName, 'w') as f:
		for line in new:
			f.write(line + '\n')


def main():
	lines = readFile('LINE-Viki.txt')
	new = split(lines)
	# writeFile('output.txt', new)

main()