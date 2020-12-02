
def inout():
    #  simple input and output with a text file
    my_file = open("text.txt")   # can also put file location
    #  print(my_file)
    print(my_file.read())
    print(my_file.read())    # this does not print because the cursor is @ EOF
    my_file.seek(0)  # put it back to start
    print(my_file.read())   # can print again
    my_file.seek(0)
    print(my_file.readlines())
    my_file.close()
    with open("text.txt") as my_new_file:  # this closes the file at the end
        contents = my_new_file.read()
    print(contents)

    with open("text.txt", mode="r") as myfile:  # mode r - read; w - write; a - append; r+ = read and write; w+ - write and read [overwrites the existing file or creates a new one]
        contents = myfile.read()
    print(contents)
    return


if __name__ == "__main__":
    inout()
    print("-----")
