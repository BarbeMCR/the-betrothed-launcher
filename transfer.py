import os
import shutil

"""The 'transfer' command."""

def transfer(installation, target):
    """Copy savefiles between installations.
    
    Arguments:
    installation -- the installation to copy savefiles from
    target -- the installation to copy savefiles to
    """
    if os.path.isdir('./'+installation):
        if os.path.isdir('./'+target):
            if os.path.isdir('./'+installation+'/data'):
                if os.path.isdir('./'+target+'/data'):
                    count = 0
                    for file in os.scandir('./'+installation+'/data'):
                            if file.path.endswith(('.dat', '.dir', '.bak', '.checksum')):
                                try:
                                    shutil.copyfile(file.path, './'+target+'/data/'+file.name)
                                    count += 1
                                except OSError:
                                    print(f"Could not copy {file.name}")
                    print(f"Successfully copied {count//4} savefile(s).")
                else:
                    print("Target does not support savefiles.")
            else:
                print("Installation does not support savefiles.")
        else:
            print("Could not find target.")
    else:
        print("Could not find installation.")