import pathlib
import re
from nltk.stem import PorterStemmer
import collections
from collections import defaultdict
import time
import math

# Initialization of dictionaries and functions

stopWordList = []
word_dict = defaultdict(int)
docNum_dict = {}
forward_index_dict = {}
inverted_index_dict = {}
docCountForIndex = 1

ps = PorterStemmer()
sortedInvertedIndex = {}
sortedForwardIndex = {}
normalizedDoc = {}
tf_idf_dict = {}
query_forward_index_dict = {}
score  = defaultdict(int)

#Initializing the present to estimate the total time taken for execution
start_time = time.time()

# Loading all the stopwordlist elements in text file to a list
with open('stopwordlist.txt', 'r') as f:
    for line in f:
        for word in line.split():
            stopWordList.append(word)


# This  method is implemented for extracting both doc numbers and the text of each file in to lists
def extractingdata(filepathdoc):
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


currentDirectory = pathlib.Path('.')
# For loop iterates thorugh all the files from ft911_1 to ft9111_15
extractedTextList = []
extractedDocNumList = []
for i in range(1):
    filepath = str(currentDirectory) + '/testing/ft911_' + str(i + 1)
    TextList, docNumlist = extractingdata(filepath)
    # Extracting all the text into list and documnet number to another for all the files present
    extractedTextList = extractedTextList + TextList
    extractedDocNumList = extractedDocNumList + docNumlist


# Removing duplicated elements in list using set function
duplicatesRemoved = list(set(extractedTextList))
# Then the tokens are sorted in alphabetic order
FinalSortedList = sorted(duplicatesRemoved)

wordCounter = 1
DocCounter = 1
# Inserting the word tokens into the dictionary file
for textToken in FinalSortedList:
    # With key as Word Index and value as word token
    word_dict[textToken] = wordCounter
    wordCounter = wordCounter + 1
# Inserting the Document number and its index into the dictionary file
for DocNumString in extractedDocNumList:
    docNum_dict[DocNumString] = DocCounter
    DocCounter = DocCounter + 1

# Initializing the forward index text file
forward_file = open("test_forward_index.txt", "w")

# This  method is implemented for extracting both doc numbers and the text of each file in to lists
def indexingEachTerm(filepathdoc):
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
        #print(x)
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


currentDirectory = pathlib.Path('.')
# For loop iterates thorugh all the files from ft911_1 to ft9111_15
for i in range(1):
    filepath = str(currentDirectory) + '/testing/ft911_' + str(i + 1)
    forwardIndex = indexingEachTerm(filepath)

inv_indx = defaultdict(int)
for key, value in forward_index_dict.items():
    #print(key)
    for innerkey, innervalue in value.items():
        intermediate_dict = {}

        if (inv_indx[innerkey] == 0) :
            inv_indx[innerkey] = {key:innervalue}
        elif(inv_indx[innerkey] != 0) :
            intermediate_dict = inv_indx[innerkey]
            intermediate_dict.update({key: innervalue})
            inv_indx[innerkey] = intermediate_dict

#sorting inner elements in forward index
for key, value in forward_index_dict.items():
    intermediate_forward_dict = {}
    for innerkey in sorted(value.items()):
        intermediate_forward_dict.update({innerkey[0]: value[innerkey[0]]})
    sortedForwardIndex.update({key : intermediate_forward_dict})

#sorting inverted index and its inner elements
for key in sorted(inv_indx.items()):
    intermediate_inverted_dict = {}
    wordIdFreq = inv_indx[key[0]]
    for innerkey in sorted(inv_indx[key[0]].items()):
        intermediate_inverted_dict.update({innerkey[0] : wordIdFreq[innerkey[0]]})
    sortedInvertedIndex.update({key[0] : intermediate_inverted_dict})


# Writting the token and its index into text file
text_file = open("test_parser_output.txt", "w")
for key, value in word_dict.items():
    text_file.write(str(value) + "         " + str(key) + '\n')

# Then writting the doc number  and its index into same file
for key, value in docNum_dict.items():
    text_file.write(str(value) + "         " + str(key) + '\n')

# Then writting the doc number  and its index into same file
for key, value in sortedForwardIndex.items():
    forward_file.write(str(key) + "         " + str(value) + '\n')

inverted_file = open("test_inverted_index.txt", "w")
# Then writting the doc number  and its index into same file
for key, value in sortedInvertedIndex.items():
    inverted_file.write(str(key) + "         " + str(value) + '\n')


for key, value in sortedForwardIndex.items():
    sumofsquares = 0
    for innerkey, innervalue in value.items():
        #print(innervalue)
        sumofsquares = sumofsquares + pow(innervalue, 2);
    sqrsum = math.sqrt(sumofsquares)
    #print(sqrsum)
    normalizedDoc[key] = sqrsum

norm_doc = open("normalized_index.txt", "w")
# Then writting the doc number  and its index into same file
for key, value in normalizedDoc.items():
    norm_doc.write(str(key) + "         " + str(value) + '\n')

# N = len(sortedForwardIndex)
# for key, value in sortedInvertedIndex.items():
#     df = len(value)
#     #print(df)
#     for innerkey, innervalue in value.items():
#         multiplied = math.log(N / df, 10)
#
#         calculated_tf_idf = innervalue * multiplied
#         normtf = calculated_tf_idf / normalizedDoc[innerkey]
#         value[innerkey] = normtf #danger overriding inverted index file
#         tf_idf_dict[key] = value





# tf_idf = open("tf_idf_index.txt", "w")
# # Then writting the doc number  and its index into same file
# for key, value in tf_idf_dict.items():
#     tf_idf.write(str(key) + "         " + str(value) + '\n')


#############################################################################
# This  method is implemented for extracting both doc numbers and the text of each file in to lists


totalDoc = ""
queryNumber = []
with open(str(currentDirectory) + '/Proj3/testTopics.txt', "r+") as fp:
    line = fp.readline()
    counter = 1
    while line:
        stripedString = line.strip() + " "
        totalDoc = totalDoc + stripedString
        if "<num>" in stripedString:
            querynum = re.sub('[^0-9]', '', stripedString)
            queryNumber.append(querynum)
            counter = counter + 1
        line = fp.readline()
Title = re.findall(r'<title>(.*?)<desc>', totalDoc)
Description = re.findall(r'<desc> Description:(.*?)<narr>', totalDoc)
Narrative = re.findall(r'<narr> Narrative:(.*?)</top>', totalDoc)


def extractDifferentQuery(TotalText):
    QueryCountForIndex = 1

    for x in range(len(TotalText)):
        cnt = collections.Counter()
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
        # frequency counting using counter method from collections
        for wordmatched in stemmedList:
            cnt[wordmatched] += 1
        tokendict = dict(cnt)
        query_forward_index_dict[QueryCountForIndex] = tokendict
        QueryCountForIndex = QueryCountForIndex + 1
    return query_forward_index_dict

##################################################################################

queryResults = open("query_output.txt", "w")
QueryIndexForTitle = extractDifferentQuery(Title)
N = len(sortedForwardIndex)
querycount = 0
for querYIdinDict in QueryIndexForTitle.keys():
    for queryTerm, tfQ in QueryIndexForTitle[querYIdinDict].items():
        queryId = word_dict[queryTerm]

        if queryId != 0:
            df = len(sortedInvertedIndex[queryId])
            for inverKey, tfD in sortedInvertedIndex[queryId].items():
                idf = math.log(N / df, 10)
                tfidf = ((tfD * idf) * (tfQ * idf))
                score[inverKey] += tfidf / normalizedDoc[inverKey]

    counterRank = 1


    for key, value in sorted(score.items(), key=lambda kv: kv[1], reverse=True):
        queryResults.write(str(key) + " " + str(counterRank) + " " + str(value) + " " + queryNumber[querycount] + '\n')
        print(str(key) + " " + str(counterRank) + " " + str(value) + " " + queryNumber[querycount] + '\n')
        counterRank = counterRank + 1
    score.clear()
    querycount = querycount + 1
##########################################################################################





queryResults.close()

forward_file.close()
inverted_file.close()
text_file.close()
#tf_idf.close()
norm_doc.close()
filepath = str(currentDirectory) + '/Proj3/main.qrels'
referenceQueryDoc = []
with open(filepath) as fp:
    line = fp.readline()
    while line:
        stripedString = line.strip().split(" ")
        querydocindicated = stripedString[2].split("-")
        if "FT911" in querydocindicated[0]:
            referenceQueryDoc.append(stripedString)
        line = fp.readline()


print("--- %s Secs ---" % (time.time() - start_time))

exit = True;
while(exit):
    queryNumberToEvaluate = input("\n\n Please select a query number 352 353 354 359  ")
    print("Please select what all should be included in query")
    options = int(input("\n 1==> Title only,  2==> Narrative + Title , 3==> Desc + Title, 4==> All"))

    if options == 1:
        queryGiven = Title
    elif options == 2:
        queryGiven = []
        for x in range(len(Title)):
            stringconc = str(Title[x] +" "+ Narrative[x])
            queryGiven.append(stringconc)

    elif options == 3:
        queryGiven = []
        for x in range(len(Title)):
            stringconc = str(Title[x] + " " + Description[x])
            queryGiven.append(stringconc)

    else:
        queryGiven = []
        for x in range(len(Title)):
            stringconc = str(Title[x] + " " + Description[x] + " " + Narrative[x])
            queryGiven.append(stringconc)

    indexOfQuery = queryNumber.index(queryNumberToEvaluate)+1
    print(indexOfQuery)
    QueryIndex = extractDifferentQuery(queryGiven)
    N = len(sortedForwardIndex)
    for queryTerm, tfQ in QueryIndex[indexOfQuery].items():
        queryId = word_dict[queryTerm]

        if queryId != 0:
            df = len(sortedInvertedIndex[queryId])
            for inverKey, tfD in sortedInvertedIndex[queryId].items():
                idf = math.log(N / df, 10)
                tfidf = ((tfD * idf) * (tfQ * idf))
                print(tfidf)
                score[inverKey] += tfidf / normalizedDoc[inverKey]

    print("Scores")
    counterRank = 1
    for key, value in sorted(score.items(), key=lambda kv: kv[1], reverse=True):
        print(str(key) + " key value" +" "+str(counterRank)+" "+ str(value) +" "+ queryNumberToEvaluate)
        counterRank = counterRank + 1


    numberofDocGiven = 0
    numberofRelaventDocsGiven = 0
    truePositive =0
    for x in range(len(referenceQueryDoc)):
        if queryNumberToEvaluate == referenceQueryDoc[x][0]:
            numberofDocGiven += 1
            print(referenceQueryDoc[x][3])
            if referenceQueryDoc[x][3] == '1':
                docnumInref = referenceQueryDoc[x][2].split("-")
                if int(docnumInref[1]) in score.keys():
                    truePositive += 1
                numberofRelaventDocsGiven += 1

    print(numberofDocGiven)
    print(numberofRelaventDocsGiven)
    print(truePositive)
    print("Precision")
    print(truePositive/len(score))
    print("Recall")
    print(truePositive/numberofRelaventDocsGiven)