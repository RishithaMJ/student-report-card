def generate_report(name, mark1, mark2, mark3):
    average = (mark1 + mark2 + mark3) / 3
    if mark1 >= 35 and mark2 >= 35 and mark3 >= 35:
        result = "pass"
    else:
        result = "Fail"

    print("\n Student Report")
    print("Student Name:", name)
    print("Marks:", mark1, mark2, mark3)
    print("Average:", average)
    print("Result:", result)

   
    with open("students.txt", "a") as file:
        file.write(f"{name},{mark1},{mark2},{mark3},{average:.2f},{result}\n")

# User input
name = input("Enter student name: ")
mark1 = int(input("Enter marks for Subject 1: "))
mark2 = int(input("Enter marks for Subject 2: "))
mark3 = int(input("Enter marks for Subject 3: "))

generate_report(name, mark1, mark2, mark3)

# Show all reports
print("\n All Student Reports:\n")
with open("students.txt", "r") as file:
    print(file.read())
