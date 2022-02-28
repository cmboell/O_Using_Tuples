"""
Assignment: File I/O using Tuples Assignment
Program: main.py
Author: Colby Boell
Last date modified: 02/28/2022

The purpose of this program is to use a function to get user input for assignment scores and
store into a tuple, then pass the tuple to another function to write a file to store the
students names and scores (append to file) and then finally call another function to
read the file and print it out, so we can see the information.
"""


# function to write the file
def write_to_file(a_tuple):
    # appends to the file
    file = open("student_info.txt", "a")
    file.write(str(a_tuple)+'\n')
    file.close()


# function that asks user to input how many scores they are wanting to enter
def get_student_info(name):
    # while loop to get an int as input
    while True:
        try:
            user_scores = int(input(f'Enter number of scores for {name}: '))
        except ValueError:
            print('Invalid, enter a number: ')
            continue
        else:
            break
    # variables
    score_list = []
    x = 0
    # while loop to fill the list with valid int
    while x != user_scores:
        try:
            score = int(input('Enter a number: '))
        except ValueError:
            print('Invalid entry')
        else:
            score_list.append(int(score))
            x = x + 1
    student_tuple = (name, score_list)
    write_to_file(student_tuple)


# function to read the file
def read_from_file():
    file = open("student_info.txt", "r")
    lines = file.readlines()
    for line in lines:
        print(line)


# main where we call functions to add info and to read file
if __name__ == '__main__':
    # writes blank file each time we run
    open("student_info.txt", "w").close()
    get_student_info('Colby')
    get_student_info('Lisa')
    get_student_info('Margot')
    get_student_info('Nala')
    read_from_file()


"""
Test:
Enter number of scores for Colby: 2
Enter a number: 34
Enter a number: 76
Enter number of scores for Lisa: e
Invalid, enter a number: 
Enter number of scores for Lisa: 3
Enter a number: 45
Enter a number: 66
Enter a number: 83
Enter number of scores for Margot: 4
Enter a number: d
Invalid entry
Enter a number: 12
Enter a number: 21
Enter a number: 34
Enter a number: 56
Enter number of scores for Nala: 1
Enter a number: 68
('Colby', [34, 76])

('Lisa', [45, 66, 83])

('Margot', [12, 21, 34, 56])

('Nala', [68])
"""
