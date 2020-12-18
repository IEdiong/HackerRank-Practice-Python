# Given the names and grades for each student in a class of N students,
# store them in a nested list and print the name(s) of any student(s)
# having the second lowest grade.

if __name__ == '__main__':
    li = list()
    N = int(input())

    if 2 <= N <= 5:
        for _ in range(N):
            name = input()
            score = float(input())
            li.append([name, score])

        # print(li)
        v = [score for name, score in li]
        # print(v)
        second = sorted(list(set(v)))[1]

        second_lowest = []
        [second_lowest.append(key) for key, value in li if value == second]

        second_lowest.sort()
        for name in second_lowest:
            print(name)

    else: print("Make your first input a number between 2 to 5, inclusive.")
