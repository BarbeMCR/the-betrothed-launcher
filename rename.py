import os

"""The 'rename' command."""

def rename(installation, name):
    """Rename an installation.
    
    Arguments:
    installation -- the target installation
    name -- the new installation name
    """
    if os.path.isdir('./'+installation):
        print("Renaming...")
        try:
            os.rename('./'+installation, './'+name)
            print(f"Successfully renamed installation {installation} to {name}.")
        except OSError as error:
            print("The installation could not be renamed. More details below.")
            print(error)
    else:
        print("Could not find installation.")