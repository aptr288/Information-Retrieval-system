import collections
import re
from nltk.stem import PorterStemmer
ps = PorterStemmer()

#This method extracts the qurery elements in each column of query and saves as list of elements in dictionary
def extractDifferentQuery(TotalText,stopWordList):
    QueryCountForIndex = 1
    query_forward_index_dict = {}
    for x in range(len(TotalText)):
        cnt = collections.Counter()
        TotalText[x] = str(TotalText[x]).strip()
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
        # frequency counting using counter method from collections
        for wordmatched in stemmedList:
            cnt[wordmatched] += 1
        tokendict = dict(cnt)
        query_forward_index_dict[QueryCountForIndex] = tokendict
        QueryCountForIndex = QueryCountForIndex + 1
    return query_forward_index_dict