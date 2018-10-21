import os
import filecmp
from dateutil.relativedelta import *
import datetime


def getData(file):
	# get a list of dictionary objects from the file
	#Input: file name
	#Ouput: return a list of dictionary objects where
	#the keys are from the first row in the data. and the values are each of the other rows

	infile = open(file, "r")
	lines = infile.readlines()
	infile.close()

	# Initializes list to hold dictionary objects
	list_of_dicts = []


	first_line = True
	for line in lines:
		# Creates list of key titles from first line of file
		# First,Last,Email,Class,DOB
		if first_line:
			key_titles = line.split(',')
			first_line = False
		else:
			# Creates list of student data from line
			values = line.split(',')
			# Initializes dictionary to hold keys
			line_dict = {}
			count = 0
			# Loops through each key title, incrementing count to match key
			for key in key_titles:
				line_dict[key] = values[count]
				count = count + 1
			# Appends new line_dict, a dictionary of studen data, to the list
			list_of_dicts.append(line_dict)
	# Returns a list of dictionaries of student data
	return list_of_dicts

def mySort(data,col):
# Sort based on key/column
#Input: list of dictionaries and col (key) to sort on
#Output: Return the first item in the sorted list as a string of just: firstName lastName
	sorted_list = sorted(data, key=lambda k: k[col])

	first_and_last = sorted_list[0]['First'] + " " + sorted_list[0]['Last']
	return first_and_last


def classSizes(data):
# Create a histogram
# Input: list of dictionaries
# Output: Return a list of tuples sorted by the number of students in that class in
# descending order
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]
	freshman_count = 0
	sophomore_count = 0
	junior_count = 0
	senior_count = 0

	# Loops through each dictionary in the list of dictionaries
	for x in data:
		# Loops through each key in the dictionary
		# Increments each class' count if key is found
		for key in x:
			if x[key] == 'Freshman':
				freshman_count = freshman_count + 1
			elif x[key] == 'Sophomore':
				sophomore_count = sophomore_count + 1
			elif x[key] == 'Junior':
				junior_count = junior_count + 1
			elif x[key] == 'Senior':
				senior_count = senior_count + 1


	class_count_list = [('Freshman', freshman_count), ('Sophomore', sophomore_count),
		('Junior', junior_count), ('Senior', senior_count)]
	class_count_list.sort(key=lambda tup: tup[1], reverse = True)

	# Returns list of tuples of the number of students in each class
	return class_count_list


def findMonth(a):
# Find the most common birth month form this data
# Input: list of dictionaries
# Output: Return the month (1-12) that had the most births in the data
	month_count_dict = { 1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0, 7 : 0,
	 8: 0, 9 : 0, 10 : 0, 11 : 0, 12 : 0}

	# Loops through each dictionary in list of dicionaries 'a'
	for x in a:
		# Splits the DOB key in dictionary at /, creating new birthday list,
		# holding month value, day value, and year value.
		birth_dates = x['DOB\n'].split('/')
		# Loops through each key in month_count_dict
		for key in month_count_dict:
			# Increments month counter
			if int(birth_dates[0]) == key:
				month_count_dict[key] = month_count_dict[key] + 1

	sorted_by_value = sorted(month_count_dict.items(), key=lambda kv: kv[1], reverse=True)
	return sorted_by_value[0][0]

def mySortPrint(a,col,fileName):
#Similar to mySort, but instead of returning single
#Student, the sorted data is saved to a csv file.
# as fist,last,email
#Input: list of dictionaries, col (key) to sort by and output file name
#Output: No return value, but the file is written

	sorted_list = sorted(a, key=lambda k: k[col])
	outFile = open(fileName,'w')

	sorted_list = sorted(a, key = lambda x: x[col])
	out_file = open(fileName, 'w')
	for a in sorted_list:
		out_file.write('{},{},{}'.format(a['First'], a['Last'], a['Email']))
		out_file.write('\n')
	out_file.close()

def findAge(a):
# def findAge(a):
# Input: list of dictionaries
# Output: Return the average age of the students and round that age to the nearest
# integer.  You will need to work with the DOB and the current date to find the current
# age in years.

	age = 0
	alist = []
	for x in a:
		date = (x['DOB\n'].split('/'))
		dates = [int(x) for x in date]
		today = datetime.date.today()
		born = datetime.date(dates[2], dates[0], dates[1])
		age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))

		alist.append(age)
	return round(sum(alist)/len(alist))



################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
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
	data2 = getData('P1DataB2.csv')
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
