class Student:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks
        self.rank = None

    def __repr__(self):
        return f"Rank {self.rank}: {self.name} (Roll {self.roll}) - {self.marks} marks"


# ---------- DIVIDE AND CONQUER: MERGE SORT ----------
def merge_sort(students):
    # Base case
    if len(students) <= 1:
        return students

    # DIVIDE
    mid = len(students) // 2
    left = merge_sort(students[:mid])
    right = merge_sort(students[mid:])

    # CONQUER + COMBINE
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    # Descending order (highest marks first)
    while i < len(left) and j < len(right):
        if left[i].marks >= right[j].marks:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


# ---------- RANK ASSIGNMENT (Tie handling) ----------
def assign_ranks(sorted_students):
    rank = 1
    for i in range(len(sorted_students)):
        # Tie case: same marks → same rank
        if i > 0 and sorted_students[i].marks == sorted_students[i - 1].marks:
            sorted_students[i].rank = sorted_students[i - 1].rank
        else:
            sorted_students[i].rank = i + 1


# ---------- MAIN ----------
if __name__ == "__main__":
    # Sample student data
    students = [
        Student(101, "Aarav",  92),
        Student(102, "Priya",  85),
        Student(103, "Rohan",  92),
        Student(104, "Sneha",  78),
        Student(105, "Kabir",  88),
        Student(106, "Ananya", 95),
        Student(107, "Vivaan", 85),
        Student(108, "Ishita", 70),
        Student(109, "Arjun",  88),
        Student(110, "Diya",   99),
    ]

    print("=== Online Exam Result Ranking System ===")
    print("Strategy: Divide & Conquer (Merge Sort)\n")

    print("--- Original Marks List ---")
    for s in students:
        print(f"  Roll {s.roll}: {s.name} - {s.marks}")

    # Step 1: Sort using Merge Sort
    sorted_students = merge_sort(students)

    # Step 2: Assign ranks
    assign_ranks(sorted_students)

    print("\n--- Final Result (Rank Wise) ---")
    print(f"{'Rank':<6}{'Roll':<8}{'Name':<10}{'Marks':<8}")
    print("-" * 35)
    for s in sorted_students:
        print(f"{s.rank:<6}{s.roll:<8}{s.name:<10}{s.marks:<8}")

    # Summary
    print("\n--- Summary ---")
    print(f"Total Students : {len(sorted_students)}")
    print(f"Topper         : {sorted_students[0].name} ({sorted_students[0].marks})")
    print(f"Average Marks  : {sum(s.marks for s in students) / len(students):.2f}")