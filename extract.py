import os
import zipfile
import string

"""The 'extract' command."""

def extract(file, path):
    """Extract BarbeMCR's The Betrothed.
    
    Arguments:
    file -- the file to extract
    """
    remove = False
    print("Checking...")
    if os.path.isfile(file):
        print("Extracting...")
        archive_file = zipfile.ZipFile(file)
        if not any([whitespace in path for whitespace in string.whitespace]):
            try:
                os.mkdir(f'./{path}')
                archive_file.extractall(f'./{path}')
                print(f"Successfully extracted file {file}")
                keep = input(f"Do you want to remove {file} (y/n)? ")
                if keep.lower() == 'y':
                    if os.path.isfile(file):
                        remove = True
                    else:
                        print("File no longer exists.")
                elif keep.lower() == 'n':
                    pass
                else:
                    print("Invalid choice. File was not deleted.")
            except OSError as error:
                print("The installation could not be created. More details below.")
                print(error)
        else:
            print("Target path contains whitespace and is not a valid installation name.")
        archive_file.close()
    if remove:
        os.remove(file)
        print(f"Removed {file}")