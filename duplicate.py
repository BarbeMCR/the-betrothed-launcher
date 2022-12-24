import shutil
import os

"""The 'duplicate' command."""

def duplicate(installation, target):
    """Duplicate an installation.
    
    Arguments:
    installation -- the installation to duplicate
    target -- the target directory
    """
    if os.path.isdir('./'+installation):
        print("Duplicating...")
        try:
            shutil.copytree('./'+installation, './'+target)
            print(f"Successfully duplicated installation {installation} to {target}.")
        except FileExistsError:
            print(f"Installation {target} already exists.")
        except OSError as error:
            print("The installation could not be duplicated. More details below.")
            print(error)
    else:
        print("Could not find installation.")