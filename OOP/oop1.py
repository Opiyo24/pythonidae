'''CLASS
    User defined data type

    Creating class
        Class ClassName:
'''


class Instructor:
    def __init__(self, instructor_name, address):
        self.name = instructor_name
        self.address = address
        self.followers = 0


instructor_1 = Instructor("Jenny", "Gurgaon") #name, address, ID, phone number, has_camera, has_lptip, has_books
print(instructor_1.name)
print(instructor_1.followers)

instructor_2 = Instructor("Payal", "Delhi") #name, address, ID, phone number, has_camera, has_lptip, has_books
print(instructor_2.name)


