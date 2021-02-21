"""Calculates grades based on inputs from the user."""

from __future__ import annotations
 
import sys
from csv import DictWriter
from typing import List, Dict, Optional


def main() -> None:
    """Entrypoint to our program."""
    categories: List[str] = []      # Categories
    all_grades: Dict[str, Dict[str, float]] = {}      # Grades
    weights: Dict[str, int] = {}        # Weights
    num_assignments: Dict[str, int] = {}
    category_avgs: Dict[str, float] = {}
    weighted_avgs: List[float] = []

    num_categories: int = int(input("# of categories in final grade breakdown: "))

    for i in range(num_categories):
        category: str = input("Name of Category: ")
        categories.append(category)
        weights[category] = int(input("Percent of Final Grade: ")) / 100
        num_assignments[category] = int(input("Number of Assignments in Category: "))

    for item in categories:
        category_grades: Dict[str, float] = {}
        grade_list: List[float] = []

        print(item + " Grades")

        for j in range(num_assignments[item]):
            assignment: str = input("Assignment Name: ")
            grade: float = float(input("Grade: "))
            category_grades[assignment] = grade
            grade_list.append(grade)

        all_grades[item] = category_grades
        category_avgs[item] = sum(grade_list) / num_assignments[item]
        weighted_avgs.append(category_avgs[item] * weights[item])

    # current_grade: float = 0.0
    final_grade: float = sum(weighted_avgs)
    letter_grade: str = get_letter_grade(final_grade)

    # print(categories)
    # print(weights)
    # print(num_assignments)
    
    print(all_grades)
    print(category_avgs)
    print(weighted_avgs)
    print(final_grade, letter_grade)


def get_letter_grade(num_grade: float) -> str:
    """Takes a numerical grade as input and returns a letter grade
    according to the UNC standard grading scale."""
    letter: str = ""

    if num_grade >= 93:
        letter = "A"
    elif num_grade >= 90:
        letter = "A-"
    elif num_grade >= 87:
        letter = "B+"
    elif num_grade >= 83:
        letter = "B"
    elif num_grade >= 80:
        letter = "B-"
    elif num_grade >= 77:
        letter = "C+"
    elif num_grade >= 73:
        letter = "C"
    elif num_grade >= 70:
        letter = "C-"
    elif num_grade >= 65:
        letter = "D+"
    elif num_grade >= 60:
        letter = "D"
    else:
        letter = "F"

    return letter


# def write_grade_table() -> None:
#     """Writes grade calculator table."""
#     file_handle = open("gradecalc.csv", "w", encoding="utf8")
#     writer = DictWriter(file_handle)
    
#     fieldnames = []

#     file_handle.close()


if __name__ == "__main__":
    main()
