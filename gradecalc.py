"""Calculates grades based on inputs from the user."""

from __future__ import annotations
 
import sys
from csv import DictWriter
from typing import List, Dict, Optional


def main() -> None:
    """Entrypoint to our program."""
    categories: List[str] = []      # Categories
    # all_grades: List[Dict] = []
    all_grades: Dict[str, Dict[str, float]] = {}      # Grades
    weights: Dict[str, int] = {}        # Weights
    num_assignments: Dict[str, int] = {}

    num_categories: int = int(input("# of categories in final grade breakdown: "))

    for i in range(num_categories):
        category: str = input("Name of Category: ")
        categories.append(category)
        weights[category] = int(input("Percent of Final Grade: "))
        num_assignments[category] = int(input("Number of Assignments in Category: "))

    for item in categories:
        category_grades: Dict[str, float] = {}

        print(item + " Grades")

        for j in range(num_assignments[item]):
            assignment: str = input("Assignment Name: ")
            category_grades[assignment] = float(input("Grade: "))

        all_grades[item] = category_grades

    print(categories)
    print(all_grades)
    print(weights)
    print(num_assignments)

    # grade_breakdown: Dict[str, int] = {}
    # nested: Dict[str, Dict[str, int]] = {}

    # num_categories: int = int(input("# of categories in final grade breakdown: "))

    # for _ in range(num_categories):
    #     type_name: str = input("Name of Category: ")
    #     grade_breakdown[type_name] = int(input("% of Final Grade: "))

    # nested["categories"] = grade_breakdown
    # print(num_categories)
    # print(grade_breakdown)
    # print(nested)


# def write_grade_table() -> None:
#     """Writes grade calculator table."""
#     file_handle = open("gradecalc.csv", "w", encoding="utf8")
#     writer = DictWriter(file_handle)
    
#     fieldnames = []

#     file_handle.close()


if __name__ == "__main__":
    main()
