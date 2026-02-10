from functions.get_files_info import get_files_info


# Test 1: Current directory
print(get_files_info("calculator", "."))

# Test 2: pkg subdirectory
print(get_files_info("calculator", "pkg"))

# Test 3: Absolute path outside working directory
print(get_files_info("calculator", "/bin"))

# Test 4: Parent directory (outside working directory)
print(get_files_info("calculator", "../"))