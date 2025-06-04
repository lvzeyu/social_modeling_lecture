import random
from pathlib import Path
from collections import defaultdict

def read_students(file_path):
    """Read students from a file, one name per line."""
    path = Path(file_path)
    print(f"Reading students from {path}")
    
    with path.open("r", encoding="utf-8") as f:
        students = [line.strip() for line in f if line.strip()]
    
    return students

def assign_presentations(students, dates):
    """Randomly assign students to the dates as evenly as possible."""
    random.shuffle(students)
    schedule = defaultdict(list)
    
    for i, student in enumerate(students):
        date = dates[i % len(dates)]
        schedule[date].append(student)
    
    return schedule

def print_schedule(schedule):
    """Print the schedule in a readable format."""
    print("\n=== Presentation Schedule ===")
    for date in sorted(schedule.keys()):
        presenters = schedule[date]
        print(f"{date} ({len(presenters)} presenters):")
        for i, student in enumerate(presenters, 1):
            print(f"  {i:>2}. {student}")
        print()

def write_schedule(schedule, output_path):
    """Write the schedule to a text file."""
    output_path = Path(output_path)
    with output_path.open("w", encoding="utf-8") as f:
        f.write("=== Presentation Schedule ===\n")
        for date in sorted(schedule.keys()):
            presenters = schedule[date]
            f.write(f"{date} ({len(presenters)} presenters):\n")
            for i, student in enumerate(presenters, 1):
                f.write(f"  {i:>2}. {student}\n")
            f.write("\n")
    print(f"\nSchedule written to {output_path}")

if __name__ == "__main__":
    # Settings
    student_file = "presentation_2025/student_list.txt"
    output_file = "presentation_2025/presentation_schedule.txt"
    presentation_dates = ["2025-06-26", "2025-07-02", "2025-07-16", "2025-07-23"]

    # Run
    students = read_students(student_file)
    schedule = assign_presentations(students, presentation_dates)
    print_schedule(schedule)
    write_schedule(schedule, output_file)
