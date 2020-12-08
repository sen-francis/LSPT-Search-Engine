import json
import os
import sys
#need to download this library on server
from bs4 import BeautifulSoup

helpstring = """usage: python3 process_html.py 'InputPath' 'OutputPath'

Argument Explanations: 
InputPath accepts a path to an input file or a directory 
containing input files (use of subdirectories is also supported, just pass the 
outer directory path). 

OutputPath defines where output files are written to. It can point to an existing
directory or if the directory is not found then a new directory with the given name
will be created.
"""




def get_list_of_filepaths(root_directory):
    file_paths = []
    for root, dirs, files in os.walk(root_directory):
        for file in files:
            full_path = os.path.join(root, file)
            file_paths.append(full_path)
    return file_paths


def pre_process(filepath):
    if filepath.rfind('/') != -1:
        filename = filepath[filepath.rfind('/')+1:]
    else:
        filename = filepath
    #make new file with name based on original name
    f = open(filename[0:-5]+"_words.txt", "w")
    #define a dictionary
    dict = {}
    with open(filepath, 'r') as file:
        soup = BeautifulSoup(file, 'html.parser')
        #get_text() finds all the words in the file, write this to new file
        f.write(soup.get_text())
        #if a title exists, adds title tag to dictionary
        if soup.title is not None:
            dict[soup.title.name] = soup.title.string
        dict['url'] = list()
        #adds all urls to the dictionary
        #assumes all links are associated with the "a" tag
        for link in soup.find_all('a'):
            if link.has_attr('href'):
                dict['url'].append(link['href'])
    f.close()
    file.close()
    return dict,filename[0:-5]+"_words.txt"


"""helper function takes an ngram and a dictionary
being used to count ngrams. If ngram in dictionary 
count is incremented by 1. If ngram isn't in dictionary
then add it as a key and set value (num occurrences) to 1."""
def handle_ngram(ngram, ngram_counter):
    entry = ngram_counter.get(ngram)
    if entry:
        ngram_counter[ngram] += 1
    else:
        ngram_counter[ngram] = 1

""""""
def parse_line(words, maxN, ngramCounters, stopWords={}, lastLine=0):
    lastStartWordIndex = max(0,len(words) - maxN + 1)
    #for last line in a document use all possible start words.
    if lastLine == 1:
        lastStartWordIndex = len(words)
    #i tracks start word lastStartWordIndex
    for i in range(lastStartWordIndex):
        startWord = words[i]
        handle_ngram(startWord, ngramCounters[0])
        #if startWord is a stop word then move on to next start word.
        if startWord in stopWords:
            continue
        else:
            ngram = startWord
            for n in range(1, maxN):
                if i + n >= len(words):
                    break
                else:
                    nextWord = words[i + n]
                    if nextWord in stopWords:
                      break
                    else:
                       ngram += " " + nextWord
                       handle_ngram(ngram, ngramCounters[n])
    return words[lastStartWordIndex:]


"""function accepts a path to an input file and a maxN value
for ngrams. It returns a list of dictionaries where each dictionary
corresponds to a n value and each key in a dictionary is a unique
ngram and the value is the number of times it occurs in the input file."""
def count_unique_ngrams(inputFilePath, maxN=3):
    ngramCounters = []
    for n in range(maxN):
        ngramCounters.append(dict())
    with open(inputFilePath, 'r') as file:
        lastWords = []
        for line in file:
            words = lastWords + line.split()
            lastWords = parse_line(words, maxN, ngramCounters, [])
        parse_line(lastWords, maxN, ngramCounters, [], 1)
    file.close()
    return ngramCounters


def process_input_file(inputFilePath, OutputDirectoryName, maxN=3):
    data, wordFilePath = pre_process(inputFilePath)
    ngramCounts = count_unique_ngrams(wordFilePath, maxN)
    data["Ngram Counts"] = ngramCounts
    if wordFilePath.rfind('/') != -1:
        wordFileName = wordFilePath[wordFilePath.rfind('/'):]
    else:
        wordFileName = wordFilePath
    outputFileName = wordFileName[0:-10] + "_output.txt"
    with open(OutputDirectoryName + "/" + outputFileName, 'w') as outputFile:
        json.dump(data, outputFile)
    outputFile.close()
    os.remove(wordFilePath)



def main():
    inputPath= sys.argv[1]
    if inputPath == "--help":
        print(helpstring)
        return
    else:
        outputPath = sys.argv[2]
        #if outputPath doesn't exist then create a directory there.
        try:
            os.mkdir(outputFileDirectory, mode=0o777)
        except:
            pass
    inputFiles = get_list_of_filepaths(inputPath)
    for filepath in inputFiles:
        process_input_file(filepath, outputPath)



if __name__ == "__main__":
    main()


