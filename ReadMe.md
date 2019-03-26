=> Implementation is done in python(3.6) <br/>
=> Porter stemmer is used from nltk library <br/>
=> Got word tokens around 32602 and number of docs 5368 <br/>
=> The stopwordlist.txt is given file containing stopwords<br/>

*******************************************************************************************

Project  Execution Procedure <br/>
===> The main code is in Indexer_main.py file.<br/>
===> Run the file and it parses query data and builds dictionary with query term and its frequency.<br/>
===> Then each topics cosine similarity is calculated for documents. <br/>
===> Finally the scores and ranks are written in text files.<br/>
===> Precision and recall are also calculated and written for every query number at end in text file. <br/>


OnlyTitleResults.txt            ===> Documents with decreasing order of scores are displayed with unique rank for each query number for Title query only here<br/>
titleWithDescriptionResults.txt ===> Title + Description query results are written here <br/>
titleWithNarrativeResults.txt   ===> Title + Narrative query results are written here <br/>
precesionRecallValues.txt       ===> all the precision and recall values are written here consolidatedly but every query has 
                                     precision and recall values after it last relevant document. <br/>

User interface <br/>

===> Have implemented the user interface for checking the score for particular query. <br/>
===> User can also provide combinations of query 1==> Title only,  2==> Narrative + Title , 3==> Desc + Title, 4==> All<br/>
===> The documents with its score relavency is displayed and the performence of the system is also displayed. <br/>

*********************************************************************************************

