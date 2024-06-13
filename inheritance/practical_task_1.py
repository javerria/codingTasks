"""
Task: 
------------------
1. Add another method in the Course class that prints the head office location: Cape Town
2. Create a subclass of the Course class named OOPCourse
3. Create a constructor that initialises the following attributes and assigns these values:
    --- "description" with a value "OOP Fundamentals"
    --- "trainer" with a value "Mr Anon A. Mouse"
4. Create a method in the subclass named "trainer_details" that prints what the 
   course is about and the name of the trainer by using the description and trainer attributes.
5. Create a method in the subclass named "show_course_id" that prints the ID number of the course: #12345
6. Create an object of the subclass called course_1 and call the following methods
   contact_details
   trainer_details
   show_course_id
   These methods should all print out the correct information to the terminal

"""

class Course:
    name = "Fundamentals of Computer Science"
    contact_website = "www.hyperiondev.com"
    head_office_location = "Cape Town"

    def contact_details(self):
        print(f"Please contact us by visiting {self.contact_website}")

    def head_office_location_details(self):
        print(f"The head office is located in {self.head_office_location}")


class OOPCourse(Course):
    def __init__(self):
        self.description = "OOP Fundamentals"
        self.trainer = "Mr Anon A. Mouse"

    def trainer_details(self):
        print(f"This course is about {self.description}")
        print(f"The trainer for this course is {self.trainer}")

    def show_course_id(self):
        print("The course ID for this course is #12345")


# Create an object of the subclass OOPCourse
course_1 = OOPCourse()

# Call the required methods on the object course_1
course_1.contact_details()  # Print contact details
course_1.trainer_details()  # Print trainer details
course_1.show_course_id()   # Print course ID
