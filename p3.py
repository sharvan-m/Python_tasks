import os
import shutil

source = "source_folder"
destination = "destination_folder"

# Ensure source folder exists (create demo files if missing)
if not os.path.exists(source):
    os.makedirs(source)
    with open(os.path.join(source, "sample1.txt"), "w") as f:
        f.write("Sample file 1 content")
    with open(os.path.join(source, "sample2.txt"), "w") as f:
        f.write("Sample file 2 content")
    print(f"Initialized '{source}' with demo files.")

# Ensure destination folder exists
if not os.path.exists(destination):
    os.makedirs(destination)

# Move all files from source to destination
files = [f for f in os.listdir(source) if os.path.isfile(os.path.join(source, f))]

if not files:
    print(f"No files found in '{source}' to move.")
else:
    for file in files:
        src_path = os.path.join(source, file)
        dest_path = os.path.join(destination, file)
        shutil.move(src_path, dest_path)
        print(f"Moved: {file} -> {destination}/")

    print("\nAll files moved successfully!")
