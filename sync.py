import os
import shutil

"""The 'sync' command."""

def sync(installation, silent=None):
    """Copy savefiles from an installation to all the others.
    
    Arguments:
    installation -- the installation to copy savefiles from
    silent -- whether to ask before overwriting existing savefiles
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
                                        if silent == 'silent':
                                            shutil.copyfile(file.path, item.path+'/data/'+file.name)
                                        else:
                                            if not os.path.isfile(item.path+'/data/'+file.name):
                                                shutil.copyfile(file.path, item.path+'/data/'+file.name)
                                            else:
                                                overwrite = input(f"{file.name} already exists in {item.name}! Do you want to overwrite it (y/n)? ")
                                                if overwrite.lower() == 'y':
                                                    shutil.copyfile(file.path, item.path+'/data/'+file.name)
                                    except OSError:
                                        print(f"Could not copy {file.name} to {item.name}")
            print(f"Successfully synced savefiles from {installation}.")
        else:
            print("Installation does not support savefiles.")
    else:
        print("Could not find installation.")