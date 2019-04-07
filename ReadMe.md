# Decisin Tree From Scratch
Implementation of decision tree from the scratch using entropy as criteria for information gain calculations.


## Getting Started
The main is file where our program execution starts.

**main.m** <br/>
Reads the dataset and does basic processing like categorical to numerical conversion. Then spilts the data  for cross validation randomly each time. Send the training data to recursive function **decisionNodeSplit** to build   the tree which returns the splitcondtions where we split the data set. Finally accuracy is calculated and decision tree is plotted. 

## Important functions 

* **decisionNodeSplit.m** <br/>
This function takes our dataset, builds the decision tree recursively and populates the split conditions. We iteratively split the dataset into left and right nodes by splitting the dataset on data point of feature with highest information gain across the dataset
and so on till we reach the leaf nodes which are pure. 
     
* **InfoGainAcrossFeatures.m** <br/>

It calculates Information gain on each feature and then return feature with highest gain among all these features and particular data point with highes gain. It uses InfoGainOnFeature.m for calculating gain on each feature. 

* **InfoGainOnFeature.m** <br/>
This function calculates on which point we get highest entropy among the data points and returns the gain and point at which
we attained the highest gain.

* **calculate_Entropy.m** <br/>
This function calculates the entropy for obtaining information gain
``` 
  A = p/(p+n);
  B = n/(p+n);
  Entropy = -A.*log2(A)-B.*log2(B);
```
* **splitDataSet.m** <br/>
This function is used for splitting the dataset based on the split point and split column and returns children datasets
left and right.

* **purityCheck.m** <br/>
This function checks if the given datasets are unique or they are still impure, if the labels are unique we return 1 and else 0. 

* **evaluation.m** <br/>
This function takes test set and tree structure as input and predicts the decisions and returns all the results.

* **Predict.m** <br/>
This function takes our data instance to predict decision, tree structure and index.  We traverse decision tree reclusively and arrive
at the leaf to return the decision.

## Example

## Tools and Dependencies  

* Built in Matlab
* Communication systems package is needed 
