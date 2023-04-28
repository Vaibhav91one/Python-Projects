import string


def longest_sub_str(my_str):
    res = 0
    count = 1
    letters = set()

    if set(my_str) == my_str:
        return len(my_str)
    if my_str == '':
        print("You have not entered anything")
        return

    for i in my_str:
        if i not in letters:
            letters.add(i)
            res = max(res, len(letters))
        else:
            letters.clear()
            letters.add(i)

    print("The longest Substring is of length", res)


my_str = str(input("Enter the string you want to check:"))
longest_sub_str(my_str)

