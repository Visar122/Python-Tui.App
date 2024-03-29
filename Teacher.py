from Person import Person

class Teacher(Person):
    def __init__(self, name, lastname, subjects):
        super().__init__(name, lastname)
        self.subjects = subjects if subjects else []  
        
    def display_info(self):
        super().display_info()
        print("fag:")
        for subject in self.subjects:
            print(f"- {subject}")
