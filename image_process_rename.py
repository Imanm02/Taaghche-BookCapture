import os

def rename_and_prepare_images():
    for path, subdirs, files in os.walk('.'):
        index_map = {}
        for file in sorted(files):
            if file.endswith(".py"):
                continue

            f_type = file.split('.')[-1].lower()
            next_index = index_map.get(f_type, 0) + 1
            new_name = f"{next_index:04d}.{f_type}"
            os.rename(os.path.join(path, file), os.path.join(path, new_name))
            index_map[f_type] = next_index

if __name__ == "__main__":
    rename_and_prepare_images()