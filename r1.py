def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf=8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	new = []
	person = None
	for line in lines:
		if line == '王軍豪':
			person = '王軍豪'
			continue
		elif line == 'Jacky Chang':
			person = 'Jacky Chang'
			continue
		elif line == 'AL':
			person = 'AL'
			continue
		elif line == '俊賢':
			person = '俊賢'
			continue
		if person:
			new.append(person + ':' + line)
	return new

def write_file(filename, lines):
	with open(filename, 'w', encoding='utf=8-sig') as f:
		for line in lines:
			f.write(line + '\n')


def main():
	lines = read_file('input.txt')
	lines = convert(lines)
	write_file('output.txt', lines)

main()