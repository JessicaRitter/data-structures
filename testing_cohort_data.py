def unique_houses(filename):
    """TODO: Return a set of student houses.

    Iterate over the cohort_data.txt file to look for all of the included house names
    and create a set called "houses" that holds those names.

    For example:

    >>> unique_houses("cohort_data.txt")
    set(['Gryffindor', 'Hufflepuff', "Dumbledore's Army", 'Ravenclaw', 'Slytherin'])

    """
    houses = set()
    filename = open(filename)
    # line = filename.split("|")
    for line in filename:
        temp_list = line.split("|")
        houses.add(temp_list[2])


    return houses

# print unique_houses("cohort_data.txt")


def sort_by_cohort(filename):
    """TODO: Return a list of all cohort lists, including ghosts but not instructors.

    Sort students by cohort, skipping instructors.

    Iterate over the data to create a list for each cohort. Puts ghosts into a
    separate list called "ghosts".

    For example:

    >>> sort_by_cohort("cohort_data.txt")
    [['Harry Potter', 'Mandy Brocklehurst', 'Ron Weasley', 'Oliver Wood', 'Colin Creevey', 'Cho Chang', 'Michael Corner', 'Draco Malfoy', 'Seamus Finnigan', 'Eddie Carmichael', 'Theodore Nott', 'Terence Higgs', 'Hermione Granger', 'Penelope Clearwater', 'Angelina Johnson', 'Dennis Creevey'], ['Neville Longbottom', 'Cedric Diggory', 'Pansy Parkinson', 'Anthony Goldstein', 'Padma Patil', 'Luna Lovegood', 'Eleanor Branstone', 'Lee Jordan', 'Marietta Edgecombe', 'Andrew Kirke', 'Ginny Weasley', 'Mary Macdonald', 'Blaise Zabini', 'Natalie McDonald', 'Adrian Pucey', 'Hannah Abbott', 'Graham Pritchard', 'Susan Bones', 'Roger Davies', 'Owen Cauldwell'], ['Laura Madley', 'Orla Quirke', 'Parvati Patil', 'Eloise Midgeon', 'Zacharias Smith', 'Cormac McLaggen', 'Lisa Turpin', 'Demelza Robins', 'Ernie Macmillan', 'Millicent Bullstrode', 'Percy Weasley', 'Jimmy Peakes', 'Justin Finch-Fletchley', 'Miles Bletchley', 'Malcolm Baddock'], ['Marcus Belby', 'Euan Abercrombie', 'Vincent Crabbe', 'Ritchie Coote', 'Katie Bell', 'Terry Boot', 'Lavender Brown', 'Gregory Goyle', 'Marcus Flint', 'Dean Thomas', 'Jack Sloper', 'Rose Zeller', 'Stewart Ackerley', 'Fred Weasley', 'George Weasley', 'Romilda Vane', 'Alicia Spinnet', 'Kevin Whitby'], ['Friendly Friar', 'Grey Lady', 'Nearly Headless Nick', 'Bloody Baron']]
    """

    filename = open(filename)

    all_students = []
    winter_16 = []
    spring_16 = []
    summer_16 = []
    fall_15 = []
    ghosts = []

    for line in filename:
        line = line.rstrip()
        temp_list = line.split("|")
        if temp_list[4] == "I":
            continue
        elif temp_list[4] == "G":
            ghosts += temp_list[0] + " " + temp_list[1]

          # all_students.append(temp_list[0] + " " + temp_list[1])
        elif temp_list[4] == "Fall 2015":
            fall_15 += temp_list[0] + " " + temp_list[1]
        elif temp_list[4] == "Summer 2016":
            summer_16 += temp_list[0] + " " + temp_list[1]
        elif temp_list[4] == "Spring 2016":
            spring_16 += temp_list[0] + " " + temp_list[1]
        elif temp_list[4] == "Winter 2016":
            winter_16 += temp_list[0] + " " + temp_list[1]


    all_students = winter_16 + spring_16 + summer_16 + fall_15


    return all_students

print sort_by_cohort("cohort_data.txt")


# test = ['Harry', 'Potter', 'Gryffindor', 'McGonagall', 'Fall 2015']
# test_winter = []
# print test_winter.append(test[0] + " " + test[1])
