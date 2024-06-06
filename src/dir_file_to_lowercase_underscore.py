import os
import sys


def convert_name(name: str) -> str:
    # convert to lowercase and replace spaces with underscores
    return name.lower().replace(" ", "_").replace("-", "_")


def convert_to_lowercase_and_replace_spaces(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=False):
        # rename files
        for filename in filenames:
            old_file_path = os.path.join(dirpath, filename)
            new_file_name = convert_name(filename)
            new_file_path = os.path.join(dirpath, new_file_name)

            if old_file_path != new_file_path:
                os.rename(old_file_path, new_file_path)
                print(f"renamed file: {old_file_path} -> {new_file_path}")

        # rename directories
        for dirname in dirnames:
            old_dir_path = os.path.join(dirpath, dirname)
            new_dir_name = convert_name(dirname)
            new_dir_path = os.path.join(dirpath, new_dir_name)

            if old_dir_path != new_dir_path:
                os.rename(old_dir_path, new_dir_path)
                print(f"renamed directory: {old_dir_path} -> {new_dir_path}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python dir_file_to_lowercase_underscore.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]

    if not os.path.isdir(directory_path):
        print(f"error: '{directory_path}' is not a valid directory.")
        sys.exit(1)

    convert_to_lowercase_and_replace_spaces(directory_path)
    print("conversion to lowercase and space replacement completed.")
