# Project Introductio: This is a simple plagiarism detector in Python which takes a text (file) as input and checks it as with the file to be checked as sayed by the user and reports if the files is subjected to any sort of plagiarism or not

import colored
# colored adds color to your output. It is Python library written in C Language
from colored import fg, bg, attr

# This is a more simple method of plagiarism checking. This is easy to understand but not as effiecient as the second one:
file = input("Enter the file name to verify: ")  # The file to be checked
verifyFile = open(file, "r")  # Opening the file to check
# The file to be checked from
CheckFile = input("Enter the file name to check it with: ")
CheckFileO = open(CheckFile, "r")  # Opening the file to be checked from

data = verifyFile.read()  # Reading the file from whoch we will check
Cdata = CheckFileO.read()  # Reading the file we will be checking from
if data in Cdata:  # Checking for plagiarism
    print(
        f"The file {file} is subjected to plagiarism from the file {CheckFile}. Please change it")
else:
    print(f"No plagiarism detected. Congrats!")


# You can make it more useful and effiecient or the user by making it a oneliner in the following way:

# lets make a command like this: check file.txt||file1.txt
# this command is like a terminal command which will verify the first file with the second one directly. No need of taking inputs anymore!

def checker(comd):
    try:  # Always use try/except to avoid errors
        ffile = comd.split("||")  # First splitting our command
        # Splitting the first part again as it contains two words
        init = ffile[0].split(" ")
        main = init[1]  # This is the name of the first file
        # print(main) ## For debugging
        toBeCheckedFrom = ffile[1]  # The file we will be checking from
        # print(toBeCheckedFrom) ## For debugging
        inFile = open(main, "r")  # Opening the file to be checked
        inFileRead = inFile.read()  # Reading the file to be checked
        # Opening the file to be checked from
        inFileN = open(toBeCheckedFrom, "r")
        inFileReadN = inFileN.read()  # Reading the file to be checked from
        if inFileRead in inFileReadN:  # Checking for plagiarism
            print(
                f"{fg('red_1')}Plagiarism detected in file {main} from the file {toBeCheckedFrom}{attr('reset')}")
        else:
            print(f"{fg('green_1')}No plagiarism detected{attr('reset')}")
    except Exception:
        print("Failed to load files")


command = input(f"{fg('green_1')}Enter command{attr('reset')}: ")
checker(command)
