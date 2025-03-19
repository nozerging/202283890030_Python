def studList():
    studentNames = ["Lisa", "Liam", "Leo", "Larry", "Linda"]
    print("Initial list of students:")
    for name in studentNames:
        print(f"{name} Evans")
    return studentNames

def addToList(studentNames):
    newName = input("Enter another name to this list: ")
    studentNames.append(newName)
    print("\nUpdated list of students:")
    for name in studentNames:
        print(f"{name} Evans")

if __name__ == "__main__":
    students = studList()
    
    addToList(students)
