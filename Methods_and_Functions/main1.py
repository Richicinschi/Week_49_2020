
def my_func2(s):
    # example I/O
    # I: my_func2("Anthropomorphism")
    # O: aNtHrOpOmOrPhIsM
    index_count = 0
    my_list = list(s)
    print(my_list)
    for i in my_list:
        if index_count % 2 == 0:
            my_list[index_count] = i.upper()
            index_count += 1
        else:
            my_list[index_count] = i.lower()
            index_count += 1
    s = ''.join(my_list)
    return s


def my_func(*args):
    my_list = []
    for i in args:
        if i % 2 == 0:
            my_list.append(i)
    return my_list


def solve3(*args, **kwargs):
    print(f"I would like {args[0]} {kwargs['food']}")
    return


def solve2(**kwargs):
    if "fruit" in kwargs:
        print(f"My fruit of choice is {kwargs['fruit']}")
    return


def solve(*args):
    print(args)
    return sum(args)


if __name__ == "__main__":
    x = solve(1, 2, 3, 4, 5, 6)
    print(x)
    solve2(fruit="apple", veggie="lettuce")
    solve3(10, 20, 30, fruit="orange", food="eggs", animal="dog")
