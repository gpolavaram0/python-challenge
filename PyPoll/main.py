import os
import csv

voteFilePath_csv = os.path.join("Instructions","PyPoll", "Resources", "election_data.csv")

voteFile = open(voteFilePath_csv, 'r')
voteFileReader = csv.reader(voteFile)
next(voteFileReader)
voteList = list(voteFileReader)
voteCount = 0
candidateList = [[],[]]

for row in voteList:
    voteCount += 1
    if candidateList[0].count(row[2]) == 0:
        candidateName = row[2]
        candidateList[0].append(candidateName)
        candidateList[1].append(0)
        index = candidateList[0].index(candidateName)
        candidateList[1][index] += 1
        #print(index)
        #for candidate in candidateList:

        #    if row[2] == candidate:
    else:
        candidateName = row[2]
        index = candidateList[0].index(candidateName)
        candidateList[1][index] += 1

resultCounter = 0
print("Election Results\n-------------------------")
print(f"Total Votes: {voteCount}")
print("-------------------------")

for candidates in candidateList[0]:

    print(candidateList[0][resultCounter] + ": " + str(100*candidateList[1][resultCounter]/voteCount) + "%  (" + str(candidateList[1][resultCounter]) +")")
    resultCounter += 1

winnerNo = max(candidateList[1])
winderIndex = candidateList[1].index(winnerNo)
winnerName = candidateList[0][winderIndex]

#print(candidateList)
print("-------------------------")
print("Winner: " + str(winnerName))
print("-------------------------")
