# Given the participants' score sheet for your University Sports Day,
# you are required to find the runner-up score. You are given  scores.
# Store them in a list and find the score of the runner-up.

# Generating a list with map
# list(map(function, iterable))

# Generating a list with a list comprehension
# [function(x) for x in iterable]

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    if 2 <= n <= 10:
        di = dict()
        for num in  arr[:n]:
            di[num] = di.get(num, 0) + 1
        lst_keys = list(di.keys())
        lst_keys = sorted(lst_keys, reverse=True)
        runup = lst_keys[1]

        print(arr)
        print(di)
        print(lst_keys)
        print(runup)

    else:
        print("Make your first input a number between 2 to 10, inclusive.")
