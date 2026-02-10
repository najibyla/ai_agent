from functions.run_python_file import run_python_file

# Should print calculator usage instructions
print(run_python_file("calculator", "main.py"))

# Should run the calculator with "3 + 5"
print(run_python_file("calculator", "main.py", ["3 + 5"]))

# Should run the calculator's tests successfully
print(run_python_file("calculator", "tests.py"))

# Should return an error (outside working directory)
print(run_python_file("calculator", "../main.py"))

# Should return an error (file doesn't exist)
print(run_python_file("calculator", "nonexistent.py"))

# Should return an error (not a .py file)
print(run_python_file("calculator", "lorem.txt"))