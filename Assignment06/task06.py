from typing import List, Tuple

def manage_student_database() -> None:
    students: List[Tuple[int, str]] = []
    id_counter: int = 1

    while True:
        name: str = input("Please enter the student's name (or type 'stop' to finish): ")
        if name.lower() == 'stop':
            break

        if any(student_name == name for _, student_name in students):
            print("This name is already in the list.")
            continue

        students.append((id_counter, name))
        id_counter += 1

    print("\nComplete List of Students (Tuples):")
    print(students)

    print("\nList of Students with IDs:")
    for student_id, student_name in students:
        print(f"ID: {student_id}, Name: {student_name}")

    total_students: int = len(students)
    total_name_length: int = sum(len(student_name) for _, student_name in students)
    longest_name: str = max(students, key=lambda x: len(x[1]))[1]
    shortest_name: str = min(students, key=lambda x: len(x[1]))[1]

    print(f"\nTotal number of students: {total_students}")
    print(f"Total length of all student names combined: {total_name_length}")
    print(f"The student with the longest name is: {longest_name}")
    print(f"The student with the shortest name is: {shortest_name}")

if __name__ == "__main__":
    manage_student_database()
