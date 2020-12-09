import sys
#need to download this library on server
from bs4 import BeautifulSoup
def pre_process(filename):
    #make new file with name based on original name
    f = open(filename[0:-5]+"_words.txt", "w")
    #define a dictionary
    dict = {}
    with open(filename, 'r') as file:
        soup = BeautifulSoup(file, 'html.parser')
        #get_text() finds all the words in the file, write this to new file
        f.write(soup.get_text())
        #if a title exists, adds title tag to dictionary
        if soup.title is not None:
            dict[soup.title.name] = soup.title.string
        dict['url'] = set()
        #adds all urls to the dictionary
        #assumes all links are associated with the "a" tag
        for link in soup.find_all('a'):
            if link.has_attr('href'):
                dict['url'].add(link['href'])
    f.close()
    return dict,filename[0:-5]+"_words.txt"

#print error message with proper format of command line args
if (len(sys.argv) != 2):
    print ("ERROR: Improper command line arguments\nProvide one file name to pre-process")
    quit()
dict, str = pre_process(sys.argv[1])
