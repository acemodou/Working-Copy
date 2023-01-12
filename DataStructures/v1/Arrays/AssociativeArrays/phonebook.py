student_list = []

def phone_contacts():
    '''
    Adding contact info into our phonebook 
    '''
    contact_info = {}
    phone_book = dict()
    number_of_contacts = int(input('How many contact info do you want to enter: '))
    for i in range(number_of_contacts):
        name = input("Enter contact info: ")
        number = int(input("Enter contact number: "))
        contact_info = {name:number}
        phone_book.update(contact_info)
    return phone_book

def call_back(look_up):
    '''
    Look up a name by using the phone number
    '''
    phonebook = phone_contacts()
    for name, num in phonebook.items():
        if num == look_up:
            print(f'{name} : is found in a dictionary')
            return name
    print(phonebook.get(look_up, f"{look_up} : is not found!"))

def create_student():
    name = input("Please enter the new student's name: ")
    student_data = {
        'name': name,
        'marks': []
    }
    return student_data

def add_mark(student, mark):
    student['marks'].append(mark)

def calculate_average_mark(student):
    number = len(student['marks'])
    if number == 0:
        return 0

    total = sum(student['marks'])
    return total / number

def print_student(student):
    print(f"{student['name']}, average mark: {calculate_average_mark(student)}.")

def print_student_list(students):
    for i, student in enumerate(students):
        print(f"ID: {i}")
        print_student(student)

def menu():
    selection = input("Enter 'a' to add a new student, "
                      "'p' to print the student list, "
                      "'g' to add a mark to a student, "
                      "'q' to quit. "
                      "Enter your selection: ")

    while selection != 'q':
        if selection == 'a':
            student_list.append(create_student())
        elif selection == 'p':
            print_student_list(student_list)
        elif selection == 'g':
            '''
            To get a specific student we need a student ID
            To know which student we are adding marks for
            '''
            student_id = int(input("Enter the student ID to add mark to: "))
            student = student_list[student_id]
            new_mark = int(input("Enter the new mark to be added: "))
            add_mark(student, new_mark)
        
        selection = input("Enter 'a' to add a new student, "
                      "'p' to print the student list, "
                      "'g' to add a mark to a student, "
                      "'q' to quit. "
                      "Enter your selection: ")
        

menu()
