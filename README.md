# Information Retrieval System 
* **Parsing and Text processing** <br/>
Each document is parsed from XML fromate it was saved and processed for removing irrelavent elements like **numerics**, 
words with numerics, **stopwords**. Then all words are converted to lower cases and **porter stemmer** is used to remove inflexional endings from words. These tokens are finally assigned a unique **word id**. 

* **Indexing** <br/>
Forward Index and Inverted index are built from given documents. Sample shown below. 
![alt text](https://github.com/aptr288/Information-Retrieval-system/blob/master/files/Inverted%20and%20forward%20Index.jpg)
* **Query Processing** <br/>
Query terms are processed in same manners as documents and cosine similarity is calculated for each keyword present in query with  relavent documents using forward and inverted index. Df and Idf values are calculated to better represent the words which carry more relevence and cosine similarity socre is calculated. Which finally results highest score for most relavent document for a given query. 
```idf = math.log(N / df, 10)
   tfidf = ((tfD * idf) * (tfQ * idf))
   score[inverKey] += (tfidf / normalizedDoc[inverKey])
```


## Execution Procedure 
* The main code is in **Indexer_main.py** file.
* Run the file and it parses query data and builds dictionary with query term and its frequency.
* Then each topics cosine similarity is calculated for documents. 
* Finally the scores and ranks are written in text files.
* Precision and recall are also calculated and written for every query number at end in text file. 


## User interface 
* Have implemented the user interface for checking the score for particular query. 
* User can also provide combinations of query 1==> Title only,  2==> Narrative + Title , 3==> Desc + Title, 4==> All
* The documents with its score relavency is displayed and the performence of the system is also displayed. 
![alt text](https://github.com/aptr288/Information-Retrieval-system/blob/master/files/Example.jpg)

## Software and files info  

* Implementation is done in python(3.6)
* Porter stemmer is used from nltk library
* Got word tokens around 32602 and number of docs 5368
* The stopwordlist.txt contains repeated words which carry less relavency information 









