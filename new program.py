scored_marks = float(input("Enter scored marks: "))
total_marks = float(input("Enter total marks: "))

if total_marks > 0:
    percentage = (scored_marks / total_marks) * 100
    print(f"Your percentage is: {percentage:.2f}%")
else:
    print("Total marks must be greater than zero.")
