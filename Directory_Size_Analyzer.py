import os

def human_readable(size):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024


directory = input("Enter directory path: ")

if not os.path.exists(directory):
    print("Directory does not exist.")
    exit()

folder_data = []

for root, dirs, files in os.walk(directory):
    total_size = 0

    for file in files:
        filepath = os.path.join(root, file)

        try:
            total_size += os.path.getsize(filepath)
        except PermissionError:
            pass
        except FileNotFoundError:
            pass

    folder_data.append({
        "folder": root,
        "size": total_size,
        "files": len(files)
    })

folder_data.sort(key=lambda x: x["size"], reverse=True)

print("\n===== Directory Size Report =====\n")

for item in folder_data:
    print(f"Folder : {item['folder']}")
    print(f"Files  : {item['files']}")
    print(f"Size   : {human_readable(item['size'])}")
    print("-" * 40)