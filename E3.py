import glob

myfiles = glob.glob("backup/*.txt")

for filename in myfiles:
    with open(filename, 'r') as file:
        print(file.read())