import os

"""The 'reset' command."""

def reset():
    """Delete savefiles from all installations."""
    print("You are about to reset ALL installations.")
    print("This will PERMANENTLY remove ALL savefiles from ALL installations.")
    print("This operation CANNOT BE UNDONE.")
    choice = input("Are you sure to continue (y/n)? ")
    if choice.lower() == 'y':
        for item in os.scandir('.'):
            if os.path.isdir(item.path):
                if os.path.isdir(item.path+'/data'):
                    for file in os.scandir(item.path+'/data'):
                        if file.path.endswith(('.dat', '.dir', '.bak', '.checksum')):
                            try:
                                os.remove(file.path)
                            except OSError:
                                pass
        print("Reset operation completed.")