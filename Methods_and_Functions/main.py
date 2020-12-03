def is_greater(a, b):
    if a > b:
        return True
    else:
        return False


def is_even(a):
    if a % 2 == 0:
        return True
    else:
        return False


def my_func4(a, b):
    return a + b


def my_func3(x, y, z):
    if z:
        return x
    else:
        return y


def my_func2(a):
    if a:
        return 'Hello'
    else:
        return 'Goodbye'


def my_func1(name):
    print('Hello {}'.format(name))


def my_func():
    print('Hello World')


def solve7(guess, my_list):
    if my_list[guess] == "O":
        print("Correct")
    else:
        print("DING DONG")
    return


def solve6(my_list):
    shuffle(my_list)
    guess = ""
    while guess not in ["0", "1", "2"]:
        guess = input("Pick a number: 0, 1, or 2")
    return int(guess), my_list


def solve5(my_list):
    shuffle(my_list)
    return my_list


def solve4(work_hours):
    # stock_prices = [("apple",200),("google",400),("microsoft",600)]
    # work_hours =
    curr_max = 0
    employ_of_month = ""
    for employee, hours in work_hours:
        if hours > curr_max:
            curr_max = hours
            employ_of_month = employee
    return employ_of_month, curr_max


def solve3(another_list):
    even_list = []
    for i in another_list:
        if i % 2 == 0:
            even_list.append(i)
    return even_list


def solve2(number):
    return number % 2 == 0


def solve1(name):
    print(f"Hello {name}")
    return


def solve():
    my_list = [1, 2, 3]
    print(my_list)
    my_list.append(4)
    print(my_list)
    my_list.pop()
    print(my_list)
    help(my_list.insert)
    return


if __name__ == "__main__":
    solve()
    print("\nnext\n")
    solve1("Aron")
    print("\nnext\n")
    print(solve2(5))
    print("\nnext\n")
    x = solve3([1, 21, 13, 5, 6, 8, 56, 89])
    print(x)
    x1, x2 = solve4([("Abby", 1000), ("Billy", 500), ("Cassie", 800)])
    print(x1, x2)
    print("\nnext\n")
    example_list = [1, 2, 3, 4, 5, 6, 7]
    from random import shuffle

    x2 = solve5(example_list)
    print(x2)
    print("\nnext\n")
    x3, x4 = solve6([" ", "O", " "])
    print(x3)
    print(x4)
    solve7(x3, x4)
    my_func()
    my_func1("Aron")
    my_func2(54)
    my_func3(1, 2, 3)
    my_func4(5, 8)
    is_even(5)
    is_greater(5, 9)
