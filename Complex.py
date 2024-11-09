import os

def list_files_in_directory(path='.'):
    # I created a dictionary to hold directories as keys and their files as values.
    directory_dict = {}

    # I used os.walk to go through each directory and its files.
    for root, dirs, files in os.walk(path):
        # I created a sub-dictionary for files within each directory.
        file_dict = {}
        for file_name in files:
            # I gathered each file's size and stored it as a dictionary entry.
            file_info = {
                'size': os.path.getsize(os.path.join(root, file_name))
            }
            file_dict[file_name] = file_info
        # I added the directory and its files to the main dictionary.
        directory_dict[root] = file_dict

    return directory_dict

# I printed the structured dictionary to check its nested organization.
files_dict = list_files_in_directory()
for directory, files in files_dict.items():
    print(f"Directory: {directory}")
    for file_name, info in files.items():
        print(f"  {file_name}: {info}")
