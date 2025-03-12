#Function: This program determines if a student will be admitted or rejected.
#Input: Test score and class rank
#Output: Admission status,(Admitted or Rejected)

# Interactive input statements to retrieve the student's test score and class rank
testScoreString = input("Enter the student's test score: ")
classRankString = input("Enter the student's class rank: ")

# Conversion of string representation to integer data type
testScore = int(testScoreString)
classRank = int(classRankString)

# Output converted values 
print("Test Score (as integer):", testScore)
print("Class Rank (as integer):", classRank)

# Test using admission requirements and print Accept or Reject
if testScore >= 90:
  if classRank >= 25:
    print("Accept")
  else:
    print("Reject")
else:
  if testScore >= 80:
    if classRank >= 50:
      print("Accept")
    else:
      print("Reject")
  else:
    if testScore >= 70:
      if classRank >= 75:
        print("Accept")
      else:
        print("Reject")
    else:
      print("Reject")