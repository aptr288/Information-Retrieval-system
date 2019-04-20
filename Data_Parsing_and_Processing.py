import re
from nltk.stem import PorterStemmer
import os



# This  method is implemented for extracting both doc numbers and the text of each file in to lists
def extractingdata(filepathdoc,stopWordList ):
    ps = PorterStemmer()
    totalDoc = ""
    FinalWordList = []
    docnumListForEachFile = []
    with open(filepathdoc) as fp:
        line = fp.readline()
        counter = 1
        while line:
            stripedString = line.strip() + " "
            totalDoc = totalDoc + stripedString
            if "<DOCNO>" in stripedString:
                docnum = re.search(r'<DOCNO>(.*?)</DOCNO>', stripedString).group(1)
                docnumListForEachFile.append(docnum)
                counter = counter + 1
            line = fp.readline()
    TotalText = re.findall(r'<TEXT>(.*?)</TEXT>', totalDoc)

    for x in range(len(TotalText)):
        TotalText[x] = str(TotalText[x]).strip()
        # Taking the text in between text tags and
        # ([a-z]*[A-Z]*[0-9]*-*_*)\d+(-*[a-z]*[A-Z]*[0-9]*-*_*)
        # TotalText[x] = re.sub("\w+(?:-\w+)+", " ", TotalText[x])
        # TotalText[x] = str(filter(lambda c: not c.isdigit(), TotalText[x]))
        # Removing workds with numbers in it or with hyphane
        TotalText[x] = re.sub("\w*-*\d+-*\w*", " ", TotalText[x])
        # Removing numbers if any present
        TotalText[x] = re.sub("\d+", " ", TotalText[x])
        # Removing all non alphanumeric elements along with _
        TotalText[x] = re.sub("\W+", " ", TotalText[x])
        # Finally converting all the words to lowercase
        lowercaseString = TotalText[x].lower()
        # splitting the sting along the space
        wordlist = re.split('\s+', lowercaseString)
        # Checking if the words in the list are present in stopWordList loaded to remove them
        for y in range(len(stopWordList)):
            if stopWordList[y] in wordlist:
                wordmatched = stopWordList[y]
                wordlist = list(filter(lambda x: x != wordmatched, wordlist))

        stemmedList = []
        for word in wordlist:
            stemmedList.append(ps.stem(word))
        # Removing any empty files
        stemmedList = list(filter(None, stemmedList))
        FinalWordList = FinalWordList + stemmedList
    return FinalWordList, docnumListForEachFile

