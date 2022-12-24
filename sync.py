import os
import shutil

"""The 'sync' command."""

def sync(installation):
    """Copy savefiles from an installation to all the others.
    
    Arguments:
    installation -- the installation to copy savefiles from
    """
    if os.path.isdir('./'+installation):
        if os.path.isdir('./'+installation+'/data'):
            for file in os.scandir('./'+installation+'/data'):
                if file.path.endswith(('.dat', '.dir', '.bak', '.checksum')):
                    for item in os.scandir('.'):
                        if item.name != installation:
                            if os.path.isdir(item.path):
                                if os.path.isdir(item.path+'/data'):
                                    try:
                                        shutil.copyfile(file.path, item.path+'/data/'+file.name)
                                    except OSError:
                                        pass
            print(f"Successfully synced savefiles from {installation}.")
        else:
            print("Installation does not support savefiles.")
    else:
        print("Could not find installation.")