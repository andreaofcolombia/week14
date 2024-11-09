import os

def list_files_in_directory():
    # I created an empty list to store file information as dictionaries.
    file_info_list = []

    # I looped through items in the current directory.
    for file_name in os.listdir('.'):
        # I checked if each item was a file.
        if os.path.isfile(file_name):
            # I gathered the file's path and size, and stored them in a dictionary.
            file_info = {
                'path': file_name,
                'size': os.path.getsize(file_name)
            }
            # I added each file's information to the list.
            file_info_list.append(file_info)

    return file_info_list

# I ran the function and printed the results to check the output.
files = list_files_in_directory()
for file in files:
    print(file)
