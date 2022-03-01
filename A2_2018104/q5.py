arr = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
major = ['W', 'W', 'H', 'W', 'W', 'W', 'H']
minor = ['W', 'H', 'W', 'W', 'H', 'W', 'W']

def answer(ans, scale):
	s = ""
	for i in ans:
		print (i, end=" ")
		s = s+i+'\n'
	if (scale == 'Major'):
		file = open('scaleMajor.txt', 'x')
	else:
		file = open('scaleMinor.txt', 'x')
	file.write(s)
	file.close()

def majorNotes(root):
	ans = [root]
	for i in major:
		prev_index = arr.index(ans[-1])
		if (i=='W'):
			next_index = (prev_index+2)%12
			ans.append(arr[next_index])
		else:
			next_index = (prev_index+1)%12
			ans.append(arr[next_index])
	return ans

def minorNotes(root):
	ans = [root]
	for i in minor:
		prev_index = arr.index(ans[-1])
		if (i=='W'):
			next_index = (prev_index+2)%12
			ans.append(arr[next_index])
		else:
			next_index = (prev_index+1)%12
			ans.append(arr[next_index])
	return ans

def noteCreate():
	root = input("Enter the root note: ")
	scale = input("Enter the type of scale (Major/Minor): ")
	if (scale == 'Major'):
		ans = majorNotes(root)
		answer(ans, scale)
	else:
		ans = minorNotes(root)
		answer(ans, scale)
noteCreate()