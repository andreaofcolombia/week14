import os

def list_files_in_directory(path='.'):
    # I created an empty list to store file information from the specified path.
    file_info_list = []

    # I used os.walk to handle recursion through all subdirectories.
    for root, dirs, files in os.walk(path):
        for file_name in files:
            # I gathered the path and size of each file.
            file_info = {
                'path': os.path.join(root, file_name),
                'size': os.path.getsize(os.path.join(root, file_name))
            }
            # I added the information to the list.
            file_info_list.append(file_info)

    return file_info_list

# I ran the function without arguments to use the current directory, then printed the output.
files = list_files_in_directory()
for file in files:
    print(file)
