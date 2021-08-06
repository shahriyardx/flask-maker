import os
import shutil


def empty_folder(path):
    """Clears all file of a folder"""
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print("Failed to delete %s. Reason: %s" % (file_path, e))


def go_back():
    """Go back from current directory"""
    os.chdir("..")


def create_file(name, content, replaces={}):
    """Creates a file with given content"""
    for key, value in replaces.items():
        content = content.replace(key, value)

    with open(name, "w") as file:
        file.write(content.strip())
