		ffile = comd.split("||")
		toCheck = ffile[0]
		init = ffile[0].split(" ")
		main = init[1]
		print(main)
		toBeCheckedFrom = ffile[1]
		print(toBeCheckedFrom)
		inFile = open(main, "r")
		inFileRead = inFile.read()
		inFileN = open(toBeCheckedFrom, "r")
		inFileReadN = inFileN.read()
		if inFileRead in inFileReadN:
			print(
				f"{fg('red_1')}Plagiarism detected in file {main} from the file {toBeCheckedFrom}{attr('reset')}")
		else:
			print(f"{fg('green_1')}