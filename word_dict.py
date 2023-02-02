# this program accepts input file, gets the words and outputs them according to the time they appear

file = input("enter file name: ")
try:
    fhandle = open(file)
except:
    print("file cannot be opened")
    quit()

all_words = dict()


for line in fhandle:
    line = line.rstrip()
    words = line.split()
    if len(words) < 1:
        continue
    for word in words:
        all_words[word] = all_words.get(word, 0) + 1

word_list = []
for k, v in all_words.items():

    # k,v is reversed so that it can sort the number not the word.

    entry = (v, k)
    word_list.append(entry)
print(sorted(word_list, reverse=True))
