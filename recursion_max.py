import timeit

## Find the max number in the list and output it
def recursion_max(myList, i):
	if i >= len(myList) - 1:
		return myList[i]

	else:
		n = recursion_max(myList, i + 1)

	if n > myList[i]:
		return n

	else:
		return myList[i]

## Modified list

myList = [501, 503, 1018, 25637, -12362, 0]

## Output the largest element
print("My List:", myList)
print("The largest element in the list is:", recursion_max(myList, 0))

## Output the program run time
def Program():
	y = 3.1415
	for x in range(100):
		y = y ** 0.7
	return y
print()
print('The program run time is: ')
print(timeit.timeit(Program, number=100000))
