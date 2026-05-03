students = []

def add_students():
    name = input("enter name:")
    marks = int(input("enter marks:"))
    students.append({"name": name, "marks": marks})

def view_students():
    for s in students:
        print(s["name"], s["marks"])

def find_topper():
    if students:
        topper = max(students, key = lambda s: s["marks"])
        print("topper :", topper["name"])
    else:
        print("no data")

def main():
    while True:
        print("\n1.add 2.view 3.topper 4.exit")
        choice = input("enter ur choice:")

        if choice == "1":
            add_students()
        
        elif choice == "2":
            view_students()

        elif choice =="3":
            find_topper()
        elif choice == "4":
            break
        else:
            print("invalid choice")

main()

