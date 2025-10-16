import os

folder_path = input("Input folder path: ")
files = os.listdir(folder_path)

for index, filename in enumerate(files, start=1):
    if filename.endswith(".txt"):
        new_filename = f"file{index}.txt"
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_filename)
        os.rename(old_path, new_path)
