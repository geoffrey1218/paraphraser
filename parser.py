# Takes a file name and reads the appropriate file into a dictionary
# File lines should be structured "key,<csv value list>" for optimal structuring
# input: filename - the name of the file to read in
# output: a dictionary of key words to lists of value words
def parse(filename):

    print("loading dictionary...")
    
    ref = dict()
    file = open(filename, 'r')

    for line in file:
        if line == "" or line == "\n":
            continue
        words = line.split(',']
        ref[words[0]] = words[1:]

    file.close()

    print("dictionary loaded.")

    return ref
