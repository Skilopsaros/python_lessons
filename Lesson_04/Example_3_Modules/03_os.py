import os

print(os.listdir()) # lists all files in the current directory
print()
print(os.listdir("../")) # can work with relative directories or absolute paths
print()
print(os.listdir("/home/skilopsaros/projects/python_lessons")) # won't work on other computers
print()
print(os.path.isdir("/home/skilopsaros/projects/python_lessons"))
print(os.path.isdir("/this/path/does/not/exist"))
print(os.path.isfile("03_os.py"))