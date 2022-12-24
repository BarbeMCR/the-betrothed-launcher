import shutil
import os

"""The 'uninstall' command."""

def uninstall(installation):
    """Uninstall BarbeMCR's The Betrothed.
    
    Arguments:
    installation -- the target installation
    """
    if os.path.isdir('./'+installation):
        print(f"You are about to uninstall installation {installation}.")
        print("This will completely remove ALL files related to it, INCLUDING savefiles.")
        print("This operation is PERMANENT and CANNOT BE UNDONE.")
        choice = input("Are you sure to continue (y/n)? ")
        if choice.lower() == 'y':
            print("Uninstalling...")
            try:
                shutil.rmtree('./'+installation)
                print(f"Successfully uninstalled installation {installation}.")
            except FileNotFoundError as error:
                print("The installation could not be uninstalled. More details below.")
                print(error)
    else:
        print("Could not find installation.")