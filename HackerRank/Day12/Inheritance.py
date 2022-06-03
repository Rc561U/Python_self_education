class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    #   Class Constructor
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    def __init__(self, firstName, lastName, idNumber, scores):
        self.scores = scores
        super().__init__(firstName, lastName, idNumber)


    #   Function Name: calculate
    #   Return: A character denoting the grade.
    def calculate(self):

        average = sum(self.scores) / len(self.scores)
        if 90 <= average <= 100: return 'O'
        if 80 <= average <= 90: return 'E'
        if 70 <= average <= 80: return 'A'
        if 55 <= average <= 70: return 'P'
        if 40 <= average <= 55: return 'D'
        if average < 40: return 'T'

if __name__ == '__main__':
#     firstName,lastName,idNum = input().split()
#     scores = list(map(int, input().split()))
#     s = Student(firstName, lastName, idNum, scores)
    s = Student('Anton', 'Ramancou', 174888, [50,60,70])
    s.printPerson()
    print("Grade:", s.calculate())
