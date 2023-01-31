# this program accepts a file name as input from the user opens it and prints all the lines in it

fname  = input('input file name: ')
try:
    fhandle = open(fname)
except:
    print("file could not be opened")
    quit()
for line in fhandle:
    line = line.rstrip()
    print(line)


