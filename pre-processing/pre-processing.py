import sys
import re
#need to download this library on server
from bs4 import BeautifulSoup
def pre_process(filename):
    #make new file with name based on original name
    f = open(filename[0:-5]+"_words.txt", "w")
    #define a dictionary
    dict = {}
    with open(filename, 'r') as file:
        soup = BeautifulSoup(file, 'html.parser')
        #iterate through all tags
        #NOTE: Currently this doesn't work for nested tags, I'm trying to fix this
        for tag in soup():
            if tag.name != "script":
                dict[tag.name]=tag.string
        #get_text() finds all the words in the file, write this to new file
        f.write(soup.get_text())
    f.close()
    return dict,filename[0:-5]+"_words.txt"


#print error message with proper format of command line args
if (len(sys.argv) != 2):
    print ("ERROR: Improper command line arguments\nProvide one file name to pre-process")
    quit()
dict, str = pre_process(sys.argv[1])
