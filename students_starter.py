
# store file location in a variable
file = '../student.csv'

# define an empty list of student records. This will be filled with each student record while reading the file
student_records = []


# load the list of dictionaries from file.
# this function reads each line in file one-by-one and appends every student's information into the list
def load(file = file):

    # open the file
    infile = open(file,'r')

    # read all lines in one go, except for the header. Note: this file has a header - Student,SI206,SI301,SI310
    lines = infile.readlines()[1:]
    infile.close()

    for line in lines:

        # get rid of \n
        line = line.rstrip()

        # create a dictionary with all the information

        # append the dictionary to student_records


# this function returns a list of dictionaries with student names and total marks
def get_total_marks():
    marks = []
    # loop through each student record. Add their scores in all three subjects.
    # Create another list of dictionaries with just names and total marks.
    # return the new list of dictionaries



# return top 5 students with highest scores
def top5students():

    # get total marks of all students

    # sort the list by marks in descending order

    # return top 5 students with scores


# get the name and score of the student who scored maximum in a course
def get_topper_in(course):

    max_score = 0
    student_name = ""

    # loop through the student records and get the maximum score in the course



if __name__ == '__main__':

    # read the file into dictionary
    load(file)

    # get top 5 students
    toppers = top5students()

    for topper in toppers:
        print(topper['Name'])

    # get the name of the student who scored maximum in course SI206
    course = 'SI206'

    student, score = get_topper_in(course)

    print("{0} topped {1} with score {2}".format(student, course, score))
