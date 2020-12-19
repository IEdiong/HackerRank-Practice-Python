# The provided code stub will read in a dictionary
# containing key/value pairs of name:[marks] for
# a list of students. Print the average of the
# marks array for the student name provided,
# showing 2 places after the decimal.
from decimal import Decimal

if __name__ == '__main__':
    n = int(input())
    student_marks = {}

    if 2 <= n <= 10:
        for _ in range(n):
            name, *line = input().split()
            line = line[:3]
            student_marks[name] = [float(str) for str in line]
            # scores = [float(str) for str in line]
            # student_marks[name] = scores

        query_name = input()
        avg = sum(student_marks[query_name]) / len(student_marks[query_name])
        avg = round(Decimal(avg), 2)
        print(avg)


    else: print("Make your first input a number between 2 to 10, inclusive.")
