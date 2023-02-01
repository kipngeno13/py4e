# this program accepts a file, opens it reads it line by line, splits it and determines the most occuring word

file = input("enter the file name: ")
try:
    fhandle = open(file)
except:
    print("Cannot open file")
    quit()

    
count = dict()
for line in fhandle:
    line = line.rstrip()
    words = line.split()
    if len(words) < 1:
            continue
   
    for word in words:
            count[word] = count.get(word,0) + 1


most_appearing = None
by_how_many = None


for word,number in count.items():
    if by_how_many is None or number > by_how_many :
        most_appearing = word
        by_how_many = number

    
print( most_appearing,by_how_many )
