# Function to calculate the letter grade
def get_letter_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def main():
    # Ask for student name
    name = input("Enter student name: ")

    # Collect 5 grades (no loops allowed, so do them individually)
    g1 = float(input("Enter grade 1: "))
    g2 = float(input("Enter grade 2: "))
    g3 = float(input("Enter grade 3: "))
    g4 = float(input("Enter grade 4: "))
    g5 = float(input("Enter grade 5: "))

    # Put grades in a list
    grades = [g1, g2, g3, g4, g5]

    # Calculate average
    average = sum(grades) / len(grades)

    # Get letter grade using the function
    letter = get_letter_grade(average)

    # Print results
    print("\n" + name)
    print(f"Average: {average:.1f}")
    print(f"Letter Grade: {letter}")


# Run program
if __name__ == "__main__":
    main()