# Create python code to recursively search the current directory for any files with extension(s) .png or .jpg or .jpeg (either capital or lowercase file extensions) and deletes them after prompting the user with a list of files to be deleted.#


import os


def find_files_with_extensions(directory, extensions):
    """Recursively search for files with given extensions in the directory."""
    found_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(extensions):
                found_files.append(os.path.join(root, file))
    return found_files


def main():
    # Extensions to search for
    extensions = (".png", ".jpg", ".jpeg")

    # Search for files with the given extensions in the current directory
    files_to_delete = find_files_with_extensions(".", extensions)

    if not files_to_delete:
        print("No files found with the given extensions.")
        return

    # Prompt the user with the list of files to be deleted
    print("The following files will be deleted:")
    for file in files_to_delete:
        print(file)

    choice = input("Do you want to delete these files? (yes/no): ").strip().lower()

    if choice in ["y", "yes"]:
        for file in files_to_delete:
            os.remove(file)
        print("Files deleted successfully.")
    else:
        print("Files were not deleted.")


if __name__ == "__main__":
    main()
