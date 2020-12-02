
def tof():
    #booleans are true or false statemetns
    # this is easy
    # important in control flow and logic
    #True # correct
    #true # wrong
    #False
    print(type(True))
    print(1 > 2)
    print(1 == 1)
    # b = None, in order to initialize

    return

def set_example():
    #sets are unordered collection of uniquie elements
    my_set = set()
    print(my_set)
    my_set.add(1)
    print(my_set)
    my_set.add(2)
    print(my_set)
    my_set.add(2) # it will not add another instance of 2 because it already has it
    print(my_set)
    my_list = [1,1,1,1,1,2,2,2,2,3,2,2,3,2,2,4,2,5,2,8,7,1]
    my_new_set = set(my_list) # looks like this will orderd the set automatically
    print(my_new_set) # however in reality sets do not have order, confusing right?
    return

def tup():
    #tuples are very similar to lists but they are immutable
    #once an element is inside a tuple you cannot reassign it
    #(1,2,3)
    t = (1,2,3)
    my_list = [1,2,3]
    print(type(t))
    print(type(my_list))
    lengthT = len(t)
    print(lengthT)
    lengthL = len(my_list)
    print(lengthL)
    print(t[1])
    t = ("a","a","b")
    print(t.count("a"))
    print(t.index("b"))

    # t[0] = "new" DING DONG - THIS IS WRONG
    return

def dict():
    #dictionaries
    #{"k1":"v1","k2":"v2"}
    # don't need to know what is the index you can search by key
    # you cannot order dictionaries
    my_dict = {"key1":"value1","key2":"value2"}
    print(my_dict)
    print(my_dict["key1"])
    new_dict = {"apple":2.99,"oranges":3.99,"milk":5}
    print(new_dict)
    #you can also have other data structures inside the dictionary
    d = {"k1":123,"k2":[0,1,2],"k3":{"insideKey":100}}
    print(d["k3"]["insideKey"]) #calling the inside key looks like a 2d array calling using indexing
    d2 = {"k1":100,"k2":200}
    d2["k3"] = 300
    print(d2)
    d2["k2"] = "new value"
    print(d2)
    print(d2.keys())
    print(d2.items()) #tuples
    print(d2.values())
    return

if __name__ == "__main__":
    dict()
    print("-----")
    tup()
    print("-----")
    set_example()
    print("-----")
    tof()
    print("-----")
