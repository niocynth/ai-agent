from functions.get_file_content import *

print("Result for main.py:")
print(get_file_content("calculator", "main.py"))
print("-----------------------------")
print("Result for pkg/calculator.py:")
print(get_file_content("calculator", "pkg/calculator.py"))
print("-----------------------------")
print("Result for '/bin/cat:")
print(get_file_content("calculator", "/bin/cat"))
print("-----------------------------")
print("Result for invalid file:")
print(get_file_content("calculator", "pkg/does_not_exist.py"))
print("-----------------------------")