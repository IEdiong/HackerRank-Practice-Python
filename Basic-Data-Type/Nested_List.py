# Given the names and grades for each student in a class of N students,
# store them in a nested list and print the name(s) of any student(s)
# having the second lowest grade.

if __name__ == '__main__':
    N = int(input())

    reg = list()
    for i in range(N):
        name = input()
        score = float(input())

        reg.append([name, score])

# print(name)
# print(score)
print(reg)
