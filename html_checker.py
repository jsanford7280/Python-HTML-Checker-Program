import re
import timeit

## Identifies the characters and ensures the user
## has proper tags in place. If not, it is false and outputs invalid.

def is_valid(filename):
	stack = []

	with open(filename, 'r') as f:
		data = f.read().replace('\n', '')
		tags = re.findall(r'(</?[a-z]*>)', data)

		for tag in tags:
			if tag.startswith("</"):
				if len(stack) == 0:
					return False
				else:
					stack.pop()
			elif tag.startswith("<"):
				stack.append(tag)
	return len(stack) == 0

## Asking the user for the final name

def main():
    filename = input('Please enter your file name: ')

    if is_valid(filename):
        	print('Valid HTML')
    else:
        	print('Invalid HTML')

if __name__ == '__main__':
    main()

## Outputs the program run time

def Program():
	y = 3.1415
	for x in range(100):
		y = y ** 0.7
	return y
print()
print('The program run time is: ')
print(timeit.timeit(Program, number=100000))
