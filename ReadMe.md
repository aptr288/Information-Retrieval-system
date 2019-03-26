=> Implementation is done in python(3.6)
=> Porter stemmer is used from nltk library
=> Got word tokens around 32602 and number of docs 5368
=> The stopwordlist.txt is given file containing stopwords 

*******************************************************************************************

Project 3 Execution Procedure 
===> The main code is in Indexer_main.py file.
===> Run the file and it parses query data and builds dictionary with query term and its frequency.
===> Then each topics cosine similarity is calculated for documents. 
===> Finally the scores and ranks are written in text files.
===> Precision and recall are also calculated and written for every query number at end in text file. 


OnlyTitleResults.txt            ===> Documents with decreasing order of scores are displayed with unique rank for each query number for Title query only here
titleWithDescriptionResults.txt ===> Title + Description query results are written here 
titleWithNarrativeResults.txt   ===> Title + Narrative query results are written here 
precesionRecallValues.txt       ===> all the precision and recall values are written here consolidatedly but every query has 
                                     precision and recall values after it last relevant document. 

User interface 

===> Have implemented the user interface for checking the score for particular query. 
===> User can also provide combinations of query 1==> Title only,  2==> Narrative + Title , 3==> Desc + Title, 4==> All
===> The documents with its score relavency is displayed and the performence of the system is also displayed. 

*********************************************************************************************

