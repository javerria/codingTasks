class Adult:
    def __init__(self, name, age, hair_colour, eye_colour):
        #Initialize an Adult object with name, age, hair colour, and eye colour.
        self.name = name
        self.age = age
        self.hair_colour = hair_colour
        self.eye_colour = eye_colour

    def can_drive(self):
        #Print a message indicating that the adult is old enough to drive.
        print(f"{self.name} is old enough to drive.")

class Child(Adult):
    def __init__(self, name, age, hair_colour, eye_colour):
        #Initialize a Child object as a subclass of Adult.
        super().__init__(name, age, hair_colour, eye_colour)

    def can_drive(self):
        #Print a message indicating that the child is not old enough to drive.
        print(f"{self.name} is not old enough to drive.")

def get_person_details():
    #Prompt the user to enter person's details and return them.
    while True:
        try:
            name = input("Enter person's name: ")
            age = int(input("Enter person's age: "))
            hair_colour = input("Enter person's hair colour: ")
            eye_colour = input("Enter person's eye colour: ")
            return name, age, hair_colour, eye_colour
        except ValueError:
            print("Invalid input for age. Please enter a valid integer.")

def driving_age():
    #Main function to determine if the person is old enough to drive.
    #Get person's details from user input
    name, age, hair_colour, eye_colour = get_person_details()

    # Determine if person is an Adult or Child based on age
    if age >= 18:
        person = Adult(name, age, hair_colour, eye_colour)
    else:
        person = Child(name, age, hair_colour, eye_colour)
    
    # Call the can_drive method of the person object
    person.can_drive()

# Call the driving_age function to run the program
driving_age()
