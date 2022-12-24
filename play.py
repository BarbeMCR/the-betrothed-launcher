import os
import sys

"""The 'play' command."""

def play(installation):
    """Start an installation and quit.
    
    Arguments:
    installation -- the target installation
    """
    if installation is None:
        if os.path.isfile('./.default'):
            with open('./.default') as default:
                target = default.readline()
            if os.path.isdir('./'+target):
                if os.path.isfile('./'+target+'/the_betrothed.exe'):
                    os.chdir('./'+target)
                    os.startfile('the_betrothed.exe')
                    sys.exit()
                elif os.path.isfile('./'+target+'/main.py'):
                    if sys.platform.startswith('win32'):
                        os.chdir('./'+target)
                        os.system('python main.py')
                        sys.exit()
                    elif sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
                        os.chdir('./'+target)
                        os.system('python3 main.py')
                        sys.exit()
                    else:
                        print("Unsupported platform.")
                else:
                    print("'.default' is pointing to an invalid installation. Use 'default' to replace the installation.")
            else:
                print("'.default' is configured incorrectly. Use 'default' to set a new default installation.")
        else:
            print("No default installation found. Use 'default' to set one or pass an installation name.")
    else:
        if os.path.isdir('./'+installation):
            if os.path.isfile('./'+installation+'/the_betrothed.exe'):
                os.chdir('./'+installation)
                os.startfile('the_betrothed.exe')
                sys.exit()
            elif os.path.isfile('./'+installation+'/main.py'):
                if sys.platform.startswith('win32'):
                    os.chdir('./'+installation)
                    os.system('python main.py')
                    sys.exit()
                elif sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
                    os.chdir('./'+installation)
                    os.system('python3 main.py')
                    sys.exit()
                else:
                    print("Unsupported platform.")
            else:
                print("Invalid installation. Please enter a valid BarbeMCR's The Betrothed installation name.")
        else:
            print("Could not find installation.")