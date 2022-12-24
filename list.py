import os

"""The 'list' command."""

def list(arg):
    """List BarbeMCR's The Betrothed installations.
    
    Arguments:
    arg -- the used/new argument
    """
    if arg is None:
        count = 0
        for item in os.scandir('.'):
            if os.path.isdir(item.path):
                if os.path.isfile(item.path+'/the_betrothed.exe'):
                    if os.path.isfile(item.path+'/.version'):
                        with open(item.path+'/.version') as ver_info:
                            version = ver_info.readline().rstrip()
                    else:
                        version = "unknown"
                    used = "can't save"
                    if os.path.isdir(item.path+'/data'):
                        used = "new"
                        for data in os.scandir(item.path+'/data'):
                            if data.path.endswith('.dat'):
                                used = "used"
                    print("{:<16} {:<16} {:<10} compiled (win32)".format(item.name, version, used))
                    count += 1
                elif os.path.isfile(item.path+'/main.py'):
                    if os.path.isfile(item.path+'/.version'):
                        with open(item.path+'/.version') as ver_info:
                            version = ver_info.readline()
                    else:
                        version = "unknown"
                    used = "can't save"
                    if os.path.isdir(item.path+'/data'):
                        used = "new"
                        for data in os.scandir(item.path+'/data'):
                            if data.path.endswith('.dat'):
                                used = "used"
                    print("{:<16} {:<16} {:<10} source".format(item.name, version, used))
                    count += 1
        print(f"Found {count} BarbeMCR's The Betrothed installation(s).")
    elif arg == 'used':
        count = 0
        for item in os.scandir('.'):
            if os.path.isdir(item.path):
                if os.path.isfile(item.path+'/the_betrothed.exe'):
                    if os.path.isfile(item.path+'/.version'):
                        with open(item.path+'/.version') as ver_info:
                            version = ver_info.readline()
                    else:
                        version = "unknown"
                    used = False
                    if os.path.isdir(item.path+'/data'):
                        for data in os.scandir(item.path+'/data'):
                            if data.path.endswith('.dat'):
                                used = True
                    if used:
                        print("{:<16} {:<16} {:<10} compiled (win32)".format(item.name, version, "used"))
                        count += 1
                elif os.path.isfile(item.path+'/main.py'):
                    if os.path.isfile(item.path+'/.version'):
                        with open(item.path+'/.version') as ver_info:
                            version = ver_info.readline()
                    else:
                        version = "unknown"
                    used = False
                    if os.path.isdir(item.path+'/data'):
                        for data in os.scandir(item.path+'/data'):
                            if data.path.endswith('.dat'):
                                used = True
                    if used:
                        print("{:<16} {:<16} {:<10} source".format(item.name, version, "used"))
                        count += 1
        print(f"Found {count} installation(s) with savefiles.")
    elif arg == 'new':
        count = 0
        for item in os.scandir('.'):
            if os.path.isdir(item.path):
                if os.path.isfile(item.path+'/the_betrothed.exe'):
                    if os.path.isfile(item.path+'/.version'):
                        with open(item.path+'/.version') as ver_info:
                            version = ver_info.readline()
                    else:
                        version = "unknown"
                    used = False
                    if os.path.isdir(item.path+'/data'):
                        for data in os.scandir(item.path+'/data'):
                            if data.path.endswith('.dat'):
                                used = True
                    if not used:
                        print("{:<16} {:<16} {:<10} compiled (win32)".format(item.name, version, "new"))
                        count += 1
                elif os.path.isfile(item.path+'/main.py'):
                    if os.path.isfile(item.path+'/.version'):
                        with open(item.path+'/.version') as ver_info:
                            version = ver_info.readline()
                    else:
                        version = "unknown"
                    used = False
                    if os.path.isdir(item.path+'/data'):
                        for data in os.scandir(item.path+'/data'):
                            if data.path.endswith('.dat'):
                                used = True
                    if not used:
                        print("{:<16} {:<16} {:<10} source".format(item.name, version, "new"))
                        count += 1
        print(f"Found {count} installation(s) without savefiles.")
    else:
        print("Invalid list query.")