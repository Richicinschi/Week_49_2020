
def assessment6():
    st = 'Create a list of the first letters of every word in this string'
    x = st.split()
    for i in x:
        print(i[0])
    return


def assessment5():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0 and i % 5 != 0:
            print("Fizz")
        elif i % 3 != 0 and i % 5 == 0:
            print("Buzz")
        else:
            print(i)
    return


def assessment4():
    st = 'Print every word in this sentence that has an even number of letters'
    mylist = st.split()
    for i in mylist:
        if len(i) % 2 == 0:
            print(i)
    return


def assessment3():
    mylist = [x for x in range(1, 51) if x % 3 == 0]
    print(mylist)
    return


def assessment2():
    for i in range(0, 11):
        if i % 2 == 0:
            print(i)
    return


def assessment1():
    st = 'Print only the words that start with s in this sentence'
    x = st.split()
    for i in x:
        if i[0].lower() == "s":
            print(i)
    return


if __name__ == "__main__":
    assessment1()
    print("\nnext\n")
    assessment2()
    print("\nnext\n")
    assessment3()
    print("\nnext\n")
    assessment4()
    print("\nnext\n")
    assessment5()
    print("\nnext\n")
    assessment6()
