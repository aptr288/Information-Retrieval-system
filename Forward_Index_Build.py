# This  method is implemented for building the forward index for each docs
import collections
import re
from nltk.stem import PorterStemmer

forward_index_dict = {}
docCountForIndex = 1

def indexingEachTerm(filepathdoc,stopWordList,word_dict):
    global docCountForIndex
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
        print(x)
        cnt = collections.Counter()
        TotalText[x] = str(TotalText[x]).strip()
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
        # FinalWordList = FinalWordList + wordlist
        # FinalWordList = list(filter(None, FinalWordList))
        ps = PorterStemmer()
        stemmedList = []
        # Stemming the words
        for word in wordlist:
            stemmedList.append(ps.stem(word))
        stemmedList = list(filter(None, stemmedList))
        #frequency counting using counter method from collections
        for wordmatched in stemmedList:
            cnt[wordmatched] += 1
        tokendict = dict(cnt)
        index_map = {}
        # building forward index
        for key, value in tokendict.items():
            index_map[word_dict[key]] = value
        forward_index_dict[docCountForIndex]= index_map
        docCountForIndex = docCountForIndex + 1

    return forward_index_dict