class Instructor:
    followers = 0 #CLASS OBJECT VAIABLE
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def display(self, subject_name):
        print("Hi, I am {} and I teach {}".format(self.name, subject_name))

    def update_followers(self):
        self.followers += 1

instructor_1 = Instructor("Jenny", "Gurgaon")
print(instructor_1.name)
instructor_1.display("Python")

instructor_2 = Instructor("Jiya", "Gurgaon")
instructor_2.update_followers()
print("{} has {} followers".format(instructor_2.name, instructor_2.followers))