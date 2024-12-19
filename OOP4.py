class string():
    def __init__(self):
        self.str1=""
    def get_string(self):
        self.str1=input("Enter string: ")
    def print_string(self):
        print("Result is:",self.str1.upper())
sr1=string()

sr1.get_string()
sr1.print_string()

