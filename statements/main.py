
def statements():
    #if
    #elif
    #else
    if 2 < 3:
        print("2 < 3 indeed")
    else:
        print("not true")

    # loops FOR
    my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]
    for x in my_list:
        if x % 2 == 0:
            print(x)

    for _ in "hello world!":
        print("cool")

    tup = (1,2,3)
    for x in tup:
        print(x)



    my_list = [(1,2),(3,4),(5,6),(7,8)]
    print(len(my_list))
    for item in my_list:
        print(item)
    #tuple unpacking below
    for a,b in my_list:
        print(a)
        print(b)
    my_list = [(1,2,3,4),(5,6,7,8),(9,10,11,12)]
    for a,b,c,d in my_list:
        print(a,b,c,d)

    d = {"k1":1, "k2":2, "k3":3}
    for x in d.items():
        print(x)
    for x in d.values():
        print(x)
    #tup unpacking in dict
    for x,y in d.items():
        print(x,y)

    # while loops
    j = 0
    while j < 25:
        j += 1
    else:
        print("done")
    return

    # break will get out of the current closest enclosing loop
    # continue will go to the top of the closest enclosing loop
    # pass does nothing at all


if __name__ == "__main__":
    statements()
    print("-----")
