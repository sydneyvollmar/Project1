import os
import filecmp
from dateutil.relativedelta import *
from datetime import date

# Sydney Vollmar

def getData(file):
# get a list of dictionary objects from the file
#Input: file name
#Ouput: return a list of dictionary objects where
#the keys are from the first row in the data. and the values are each of the other rows

	inFile = open(file)
	line = inFile.readline()

	# list of dictionaries
	lstDict = []

	headers = line.split(",")
	h1 = headers[0]
	h2 = headers[1]
	h3 = headers[2]
	h4 = headers[3]
	h5 = headers[4].strip()

	# move on from first line before collecting data
	line = inFile.readline()

	# while there is a line
	while line:
		dictVals = {}
		values = line.split(",")
		firstName = values[0]
		lastName = values[1]
		email = values[2]
		year = values[3]
		dob = values[4].strip()

		# set up dictionary
		dictVals[h1] = firstName
		dictVals[h2] = lastName
		dictVals[h3] = email
		dictVals[h4] = year
		dictVals[h5] = dob
		lstDict.append(dictVals)

		# read the next line
		line = inFile.readline()

	return lstDict


def mySort(data,col):
# Sort based on key/column
#Input: list of dictionaries and col (key) to sort on
#Output: Return the first item in the sorted list as a string of just: firstName lastName

	# sort based on key given in parameters
	newLst = sorted(data, key = lambda d : d[col])

	# get first dictionary in list
	firstDict = newLst[0]

	# assign first dictionary in list to vals of first and last name
	firstName = firstDict['First']
	lastName = firstDict['Last']

	# return desired formatting correctly sorted
	return firstName + " " + lastName


def classSizes(data):
# Create a histogram
# Input: list of dictionaries
# Output: Return a list of tuples sorted by the number of students in that class in
# descending order
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]

	# empty dictionary for holding only classes/grades
	sortClass = {}

	# loops through each dictionary in list
	for d in data:
		grade = d['Class']
		# if class already in the new dictionary, increase the count
		if grade in sortClass:
			sortClass[grade] += 1
		# if class is not in new dictionary, start count at 1
		else:
			sortClass[grade] = 1

	# new list to add new tuples to
	lstClass = []
	for elem in sortClass:
		# creates tuples with desired info from classes dicitonary
		lstClass.append((elem, sortClass[elem]))

	# sorts tuples from greatest to least
	lstSorted = sorted(lstClass, key = lambda d : d[1], reverse = True)

	# returns list of tuples
	return lstSorted


def findMonth(a):
# Find the most common birth month form this data
# Input: list of dictionaries
# Output: Return the month (1-12) that had the most births in the data

	# new dictionary to use for months
	sortMonths = {}

	# index through dictionaries in the list given
	for d in a:
		dob = d['DOB']
		# splits dob at each / to get just the month
		month = dob.split("/")[0]
		# if month in dictionary, increase count by 1
		if month in sortMonths:
			sortMonths[month] += 1
		# if month not in new dictionary, start count at 1
		else:
			sortMonths[month] = 1

	lstMonths = []
	# index through elements in diciontary of month totals
	for elem in sortMonths:
		lstMonths.append((elem, sortMonths[elem]))

	# sorts the new list of months from highest to lowest frequency month
	lstSorted = sorted(lstMonths, key = lambda d : d[1], reverse = True)

	return int(lstSorted[0][0])

def mySortPrint(a,col,fileName):
#Similar to mySort, but instead of returning single
#Student, the sorted data is saved to a csv file.
# as fist,last,email
#Input: list of dictionaries, col (key) to sort by and output file name
#Output: No return value, but the file is written

	# sorts list given by dictionary key given
	newLst = sorted(a, key = lambda d : d[col])

	# says writing to this particular file name
	outFile = open(fileName, "w")

	# loops through each dictionary in sorted list and outputs correct info
	for student in newLst:
		outFile.write(student['First'] + ',' + student['Last'] + ',' + student['Email'] + '\n')

	outFile.close()

def findAge(a):
# def findAge(a):
# Input: list of dictionaries
# Output: Return the average age of the students and round that age to the nearest
# integer.  You will need to work with the DOB and the current date to find the current
# age in years.

	pass


################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

# We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ", end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),50)

	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',25)
	total += test(mySort(data2,'First'),'Adam Rocha',25)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',25)
	total += test(mySort(data2,'Last'),'Elijah Adams',25)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',25)
	total += test(mySort(data2,'Email'),'Orli Humphrey',25)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],25)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],25)

	print("\nThe most common month of the year to be born is:")
	total += test(findMonth(data),3,15)
	total += test(findMonth(data2),3,15)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,20)

	print("\nTest of extra credit: Calcuate average age")
	total += test(findAge(data), 40, 5)
	total += test(findAge(data2), 42, 5)

	print("Your final score is " + str(total))

# Standard boilerplate to call the main() function that tests all your code
if __name__ == '__main__':
    main()
