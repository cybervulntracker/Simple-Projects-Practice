import os, time

folder = "test_folder"

# create folder if it doesn't exist
if not os.path.exists(folder):
    os.makedirs(folder)

old_files = set(os.listdir(folder))

while True:
    time.sleep(5)
    new_files = set(os.listdir(folder))

    deleted = old_files - new_files
    if deleted:
        print("Deleted files:", deleted)

    old_files = new_files