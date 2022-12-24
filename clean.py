import os

"""The 'clean' command."""

def clean(installation):
    """Delete savefiles from an installation.
    
    Arguments:
    installation -- the target installation
    """
    if os.path.isdir('./'+installation):
        if os.path.isdir('./'+installation+'/data'):
            print(f"You are about to clean installation {installation}.")
            print("This will PERMANENTLY remove ALL savefiles. This operation CANNOT BE UNDONE.")
            choice = input("Are you sure to continue (y/n)? ")
            if choice.lower() == 'y':
                count = 0
                for file in os.scandir('./'+installation+'/data'):
                    if file.path.endswith(('.dat', '.dir', '.bak', '.checksum')):
                        try:
                            os.remove(file.path)
                            count += 1
                        except OSError:
                            print(f"Could not delete {file.name}")
                print(f"Successfully deleted {count//4} savefile(s).")
        else:
            print("Installation does not support savefiles.")
    else:
        print("Could not find installation.")