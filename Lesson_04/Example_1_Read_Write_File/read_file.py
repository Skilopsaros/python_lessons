def read_file():
    with open("my_file_one") as file:
        my_lines = file.readlines()
        print(my_lines)

def write_file():
    with open("my_file_two", "w") as file:
        file.write("Hello this is a new file")
        # file.write("Hello this is a new file")

def append_to_file():
    with open("my_file_one", "a") as file:
        file.write("Appending...")

read_file()
# write_file()
# append_to_file()