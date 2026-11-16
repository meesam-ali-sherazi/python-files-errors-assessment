
import csv

# Read attendance records
try:
    with open("attendance.txt", "r") as file:
        original_names = file.readlines()

    # Count original non-empty records
    original_count = len([
        name for name in original_names if name.strip()
    ])

    # Clean names using list comprehension
    cleaned_names = [
        name.strip().title()
        for name in original_names
        if name.strip()
    ]

    # Remove duplicate names using set
    unique_names = set(cleaned_names)

    # Sort names alphabetically
    final_names = sorted(unique_names)

    # Save cleaned attendance in CSV file
    with open("attendance_clean.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(["Student Name"])

        for name in final_names:
            writer.writerow([name])

    # Display results
    print("\n===== ATTENDANCE REPORT =====")

    print("Original Records:", original_count)

    print("Unique Students:", len(unique_names))

    print("\n===== CLEANED ATTENDANCE LIST =====")

    for name in final_names:
        print(name)

    print("\nCleaned attendance saved successfully!")

except FileNotFoundError:
    print("Error: attendance.txt file not found!")

