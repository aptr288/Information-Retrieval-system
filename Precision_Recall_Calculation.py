# precision and recall calculation is done in this function
def calPrecisionRecal(scorecalculated,queryNumberToEvaluateOn,referenceQueryDoc, score):
    numberofDocGiven = 0
    numberofRelaventDocsGiven = 0
    truePositive = 0
    for x in range(len(referenceQueryDoc)):
        if queryNumberToEvaluateOn == referenceQueryDoc[x][0]:
            numberofDocGiven += 1
            if referenceQueryDoc[x][3] == '1':
                docnumInref = referenceQueryDoc[x][2].split("-")
                if int(docnumInref[1]) in scorecalculated.keys():
                    truePositive += 1
                numberofRelaventDocsGiven += 1

    #print(numberofDocGiven)
    #print(numberofRelaventDocsGiven)
    #print(truePositive)
    #print("Precision")
    precisionCal = truePositive / len(score)
    #print(precisionCal)
    #print("Recall")
    recallCal = truePositive / numberofRelaventDocsGiven
    #print(recallCal)
    # Reset all the values
    numberofRelaventDocsGiven = 0
    truePositive = 0
    scorecalculated.clear()
    return precisionCal, recallCal